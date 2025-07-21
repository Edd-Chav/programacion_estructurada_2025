import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            print(".:: Agregar Peliculas ::.")
            peliculas.esperarTecla()
        case "2":
            print(".:: Eliminar Peliculas ::.") 
        case "3":
            print(".:: Modificar Peliculas ::.")     
        case "4":
            print(".:: Consultar Peliculas ::.")  
        case "5":
            print(".:: Buscar Peliculas ::.") 
        case "6":
            print(".:: Vacias Peliculas ::.") 
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            input("Opción invalida vuelva a intentarlo ... por favor")