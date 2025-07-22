'''Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica la funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

sintaxis:
def nombre_funcion(parametros):
    bloque o conjunto de instrucciones

    nombre_funcion(parametros)
    
    las funciones pueden ser de hasta 4 tipos:

    Funciones de tipo procedimiento.
    1.- Funcion que no recibe parametros y no regresa el valor
    3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor


'''

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

#Llamada a la funcion
solicitar_datos1()

nomnbre3=input("¿Cual es tu nombre?")
telefono3=input("¿Cual es tu telefono?")
solicitar_datos3(nomnbre3, telefono3)

nombre2, telefono2 = solicitar_datos2()
print(f"Nombre: {nombre2} \nTelefono: {telefono2}")

nombre4=input("¿Cual es tu nombre?")
telefono4=input("¿Cual es tu telefono?")
nombre4, telefono4= solicitar_datos4(nombre4, telefono4)
print(f"Nombre: {nombre4} \nTelefono: {telefono4}")
