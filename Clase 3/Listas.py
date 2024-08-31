'''LISTAS
listas["hola, 1, True, [1,2]]
'''

'''Funciones'''

'''Introduccion a lista'''
array=["futbol", "PC", 18.5, 18, [6,7,10.4], True, False]
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])

#Cantidad de datos que  cuenta el array
print(len(array))
#Agregar un valor dentro de la lista
array.append(66)
print(array)
#Insertar datos en una posicion
array.insert(1,88)
print(array)
#InsertR MAS DE UN DATO AL FINAL
array.extend([1,88,True,100])
print(array)



