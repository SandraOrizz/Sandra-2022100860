#!/usr/bin/env ython3
from flask import Flask
from flasw_swagger_ui import get_swaggerui_blueprint
from login import login

app = Flask (__name__)

##servicios rest
app.register_blueprint(login)

#definir la ruta swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json' #ruta al archivo swagger
swaggerui_blueprint = get_swaggerui_blueprint(
   SWAGGER_URL,
   API_URL,
   config={
      'app_name'= "Login API"
   }
)

app.register_blueprint(swaggerui_blueprint, url_perfix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola, Mundillop'

if __name__ == '__main__':
 
 app.run(host='0.0.0.0', debug= True, port=5001)

