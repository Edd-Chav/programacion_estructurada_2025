import peliculas_dago
import os
os.system("cls")

opcion=True
while opcion:
    os.system("cls")
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Consultar  \n 4.- Agregar Caracteristicas \n 5.- Modificar Caracteristicas \n 6.- Borrar Caracteristicas \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago.anadir_peliculas()
            peliculas_dago.mostrarpelicula()
            peliculas_dago.esperarTecla()
            
            
        case "2":
            peliculas_dago.borrar_pelicula()
            peliculas_dago.esperarTecla()
            
        case "3":
            peliculas_dago.consultar_peliculas()
            peliculas_dago.esperarTecla() 
               
        case "4":
             peliculas_dago.agregarCaracteristicaPeliculas()     
             peliculas_dago.esperarTecla()        
        case "5":
            peliculas_dago.modificarCaracteristicasPeliculas()
            peliculas_dago.esperarTecla()
        
        case "6":
            peliculas_dago.borrarCaracteristicas()
            peliculas_dago.esperarTecla()
        case "7":
            opcion=False
            peliculas_dago.borrarPantalla()    
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")