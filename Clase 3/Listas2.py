array1=["futbol", "PC", 18.6, 18, [6,7,10.4], True, False, "PC"]
array2=[200,250,"hola"]
array3=array1+array2
print(array3)

#Buscar valores dentro de un array
print("PC" in array1)

#Saber el indice donde esta lo que busco
print(array1.index("PC"))

#Cantidad de vaces que tengo el valor en mi array
print(array1.count("PC"))

#Borrar valores de un array
array1.remove("PC")
print(array1)

#Limpiar
#array.clear()
print(array1)

#cambiar la posicion
array1.reverse()
print(array1)

#ordenar de mayor a menor
array4=[1,2,8,-11.5]
array4.sort()
print(array4)
array4.sort(reverse=True)
