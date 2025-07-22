'''es una coleccion desordenadam inmutable y no indexada, no hay miembros duplicados.'''
import os
os.system("cls")

personas= {"Ramiro", "Choche", "Lupe"}
print(personas)
personas.add("Peje")
print(personas)
personas.pop()
personas.clear()
print(personas)
print("-----------------------")
varios={3.1416, 3, True, "Hola"}
print(varios)
