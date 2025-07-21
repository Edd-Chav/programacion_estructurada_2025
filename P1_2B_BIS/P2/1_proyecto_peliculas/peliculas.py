''' Crear un proyecyo que te permita modificar peliculas, agregar un menu de opciones que permita agredar, eliminar,
y comentar peliculas, 1.-Utiñizar funciones y mandar a llmaar desde otro archivo, 2.- Utilizar listas para almacenar los nombres
de las peliculas'''

import os
os.system("Clear")

pelicula=8
match pelicula:
    case 8:
        print("Ratatouille")
    case 14:
        print("In time")
    case 21:
       print("Moana")
    case _:
        print("Sin pelicula")

#Pelicula
if pelicula == 0:
    print("Ratatouille")
elif pelicula == 14:
    print("In time")
elif pelicula == 21:
    print("Moana")
else:
    print("Sin pelicula")


#Catalogo

tablero=4
match tablero:
    case 12 | 1 | 2: print("Terror")
    case 3 | 4 | 5: print("Comedia")
    case 6| 7 | 8: print("Suspenso")
    case 9 | 10 | 11: print("Accion")
    case _: print("No hay catalogo")

#Terror

coordenada=(0,1)
match coordenada:
    case (0.0):
        print("Coordenada origen")
    case (x,0):
        print(F"Coordenada en eje x: {x}")
    case (0,y):
        print(f"Coordenada en eje y: {y}")
    case _:
        print("No hay coordenadas")



opcion=True
while opcion:
    os.system("clear")
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            os.system("clear")
            print(".:: Agregar Peliculas ::.")
            input("Oprima cualquier tecla para continuar ...")
        case "2":
            os.system("clear")
            print(".:: Eliminar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...") 
        case "3":
            os.system("clear")
            print(".:: Modificar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            os.system("clear")
            print(".:: Consultar Peliculas ::.")
            input("Oprima cualquier tecla para continuar ...")  
        case "5":
            os.system("clear") 
            print(".:: Buscar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")
        case "6":
            os.system("clear") 
            print(".:: Vacias Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")
        case "7":
            os.system("clear")
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            os.system("clear") 
            input("Opción invalida vuelva a intentarlo ... por favor")
    


    pelicula=[]

    def borrarPantalla():
        import os
        os.system("Clear")
    
    def esperarTecla():
        print("Oprima cualquier tecla para continuar...")
        input()
    
    def agregarPeliculas():
        borrarPantalla()
        print(".:: Alta de Peliculas ::.")
        pelicula=input("Ingresa el nombre: ")
        pelicula.append(pelicula)

        def consultarPeliculas():
            borrarPantalla()
            print(".::Consultar Peliculas::.")
            print(pelicula)
 