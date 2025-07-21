#un modulo es simolmente un archivo de python que contiene funciones, clases y variables.
#un paquete es una carpeta que contiene varios modulos (archivos .py) y un archivo especial  __init__.py que le indica a pyrthon que esa carpeta debe tratarse como un paquete


import os

# 1.- Funcion que no recibe parametros y no regresa el valor
def solicitar_datos1():
    nombre = input("¿Cual es tu nombre?")
    telefono = input("¿Cual es tu telefono?")
    print(f"SOY FUNCION 1.- Tu nombre es: {nombre}, tu telefono es: {telefono}")

# 3.- Funcion que recibe parametros y no regresa valor
def solicitar_datos3(nombre, telefono):
    nombre = nombre
    telefono = telefono
    print(f"Soy funcion 3.- Tu nombre es: {nombre}, tu telefono es: {telefono}")

# 2.- Funcion que no recibe parametros y regresa valor
def solicitar_datos2():
    nombre = input("¿Cual es tu nombre?")
    telefono = input("¿Cual es tu telefono?")
    return nombre, telefono

# 4.- Funcion que recibe parametros y regresa valor
def solicitar_datos4(nombre, telefono):
    nombre=nombre
    telefono=telefono
    return nombre, telefono

def borrarPantalla():
        os.system("clear")

def esperarTecla():
    input("Presiona una tecla para continuar...")

def saludar(nombre):
     nombre=nombre
     return f"Hola, bienvenido {nombre}"
