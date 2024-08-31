
def ingresar_numeros():
    numeros = []
    while True:
        numero = input("Ingrese un numero (o 'n' para terminar): ")
        if numero.lower()=='n':
            break
        numeros.append(float(numero))
        return numeros
    def sumar_numeros(numeros):
        sumar=0
        for numero in numeros:
            suma += numero
            return sumar
        
    def calcular_promedio(numeros):
        suma=sumar_numeros(numeros)
        promedio = suma/len(numeros)
        return promedio

    def enconrar_max_min(numero):
        maximo=max(numeros)
        minimo=min(numeros)
        return maximo,minimo   
    
def main():{}
numeros= ingresar_numeros()
if len(numeros) ==0:
    print ("No se ingresaron numeros")
    return
suma=sumar_numeros(numero)
promedio=calcular_promedio(numeros)
maximo, minimo= encontrar_max_min(numeros)
mayores=numeros_may_que_promedio(numeros, promedio)

print(f"\n Numeros ingresados: {numeros}")
print(f"\n suma de los numeros: {suma}")
print(f"\n Promedio de los numeros: {promedio}")
print(f"\n Numero más grandes: {maximo}")
print(f"\n Numero más pequeño: {minimo}")
print(f"\n Numeros mayores que el promedio: {mayores}")


if __name__ == "__main__":
    main()
