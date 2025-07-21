'''Listas (array)
son colecciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valoresse hace con un indice numerico
Nota: sus valores si son modificables
La lista es una coleccion ordenada y modificable permite mienmbros duplicados.'''

#Funciones mas comunes en las listas

paises=["Mexico","Brasil","España","Canada"]

numeros=[23,12,100,34]

#ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)

print(paises)
paises.sort()
print(paises)

#añadir o ingresar o insertar elementos a la lista
#1er forma
print(paises)
paises.append("Honduras")
#2da forma
paises.insert(1,"Honduras")
print(paises)

#eliminar o borrar o quitar elementos de la lista
#1era forma con el indice
paises.pop(1)
print(paises)

#2da forma con el valor
paises.remove("Honduras")
print(paises)

#Buscar un elemento en la lista
#1era forma
resp="brasil" in paises
if resp:
    print("El pais si existe")
else:
    print("El pais no existe")

#2da forma
pais_buscar=input("dame el pais a buscar: ")
paises=["Mexico","Brasil","España","Canada"]

for i in range(0,len(paises)):
    if paises[i]==pais_buscar:
        print("si existe el pais")
    else:
        print("no existe el pais")


#cuantas veces aparece un elemento en la lista
print(f"Este numero aparece {numeros.count(12)} veces en la lista")

numeros.append(12)
print(f"Este numero aparece {numeros.count(12)} veces en la lista")

#conocer el indice de un valor
#[paises=["Mexico","Brasil","España","Canada"]

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#recorrer una lista
#1era forma
for i in paises:
    print(i)

#2da forma
for i in range(0, len(paises)):
    print(f"El valor {i} es: {paises[i]}")

#unir contenido de dos listas
#paises=["Mexico","Brasil","España","Canada"]
#numeros=[23,12,100,34]

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)

          

