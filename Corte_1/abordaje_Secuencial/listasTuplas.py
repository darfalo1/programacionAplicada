#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Asignamos los valores de la tupla
#input()
print(my_lista)         #Se imprime los valores de la lista
print(type(my_lista))   #Se imprime el tipo de la lista
print(my_lista[2])      #Se imprime la posicion 2 de la lista

print("my_lista size: ", len(my_lista)) #Se imprime el tamaño de la lista
print(my_lista[0:3])    #Imprimi los valores desde una posicion m hasta n-1
print(my_lista[:4])     #Imprime los valores  desde 0 hasta n-1

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro')
print(my_lista)


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)

print(my_lista.index('Azul'))   #Nos da la posicion de Azul

#my_lista.remove('Magenta')
my_lista.remove('Marron')       #Borra el elemento Marron
print(my_lista)

my_lista.insert(8, 'Marron')    #Inserta un elemento en dicha posicion
print(my_lista)

print(my_lista.pop())       #Borra el ultimo elemento de la lista
size = len(my_lista)        #Se guarda en una variable el tamaño de la lista
print("size = ", size)
#print(my_lista.pop(size))

my_lista_3 = my_lista*3     #Se crea otra lista con tres veces los elementos de la anterior
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_listaSort = my_lista.sort()  #Organiza los elementos en la lista, pero este metodo no retorna valor, en my_listaSort no hay valores
print(my_listaSort)
print(my_lista) #Se imprime el valor de la lista

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()       #Organiza la lista de menor a mayor
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True) #Organiza la lista de mayor a menor
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)      #Crea el objeto my_tupla con los valores de la lista
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])      #Imprime la posicion 0 de la tupla
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)       #Agrega un nuevo elmento a la tupla
print(my_tupla.count('Rojo'))   #Verifica si existe un elemento

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')  #Crea una tupla de un unico valor
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999 #Asisgan nuevos valores a la tupla
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla    
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
