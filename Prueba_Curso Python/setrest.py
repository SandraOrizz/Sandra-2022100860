
from flask import Flask, Blueprint, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import mysql.connector
from datetime import datetime
from time import sleep

app = Flask(__name__)
setrest01 = Blueprint('setrest01', __name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'curso_python'
}

@app.route('/setrest01', methods=['POST'])
def llamarServicioSet():
    codigo = request.json['codigo']
    password = request.json['password']
    
    salida = inicializarVariables(codigo, password)
    
    return jsonify({'ParmOut': salida})

def inicializarVariables(codigo, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chromedriver_path = 'C:\Users\Sandra\Desktop\Python\Prueba_Curso Python\chromedriver.exe'
    
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(15)
    
    try:
        driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')
        accesoSet(driver, codigo, password)
    except TimeoutException:
        driver.close()
        driver.quit()
        print("No se pudo abrir")
    finally:
        driver.quit()

def accesoSet(driver, codigo, password):
    url_jaguarete = 'https://jaguarete.unida.edu.py/jaguarete/Login'
    
    try:
        codigo_input = driver.find_element(By.ID, 'codigo')
        codigo_input.send_keys(codigo)
        sleep(5)
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        sleep(5)
        
        login_button = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
        login_button.click()
        sleep(5)
        
        registrar_evento(codigo, url_jaguarete)
        
    except Exception as e:
        print("ERROR EN: login, intentando cerrar el driver", str(e))
    
def registrar_evento(matricula, direccion_url):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        
        query = """INSERT INTO registro (matricula, direccion_url, fecha)
                   VALUES (%s, %s, %s)"""
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (matricula, direccion_url, fecha))
        
        conexion.commit()
    
    except mysql.connector.Error as err:
        print(f"Error al registrar en la base de datos: {err}")
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == '__main__':

    codigo = input("Ingrese su matricula: ")
    password = input("Ingrese su contraseña: ")
    
    app.register_blueprint(setrest01)
    
    inicializarVariables(codigo, password)
    
    app.run(host='0.0.0.0', port=5000)
