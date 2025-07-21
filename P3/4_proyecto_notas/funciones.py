def borrarPantalla():
    import os 
    os.system("clear")

def esperarTecla():
    input("\n\t\t..Oprima cualquier tecla para continuar...")

def menu_principal():
    print(".::Sistema de Gestion de Notas::. \n1.- Resgistro \n2.- Login \n3.- Salir")
    opcion=input("Elige una opcion").upper
    return opcion