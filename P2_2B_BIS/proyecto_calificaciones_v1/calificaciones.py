import os
os.system("cls")

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("Presiona una tecla para continuar...")

def menu_principal():
    print("\n\t\t\t`\U0001F389`\033[3m...:::::MENÚ:::::...`\U0001F389`\n\033[0m"
          "\t\t1. \U0001F4DD Añadir Calificación\n"
            "\t\t2. \U0001F50D Mostrar Calificación\n"
            "\t\t3. \U0001F464 Calcular Promedio\n")
    op=input("elige una opcion")
    return op

def anadir_calificacion(lista):
    borrarPantalla()
    print("Agregar Calificaciones: \U0001F4DD ")
    nombre = input("Ingrese el nombre del estudiante: \U0001F464 ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continuar = True
        while continuar:
            try:
                cal=float(input(f"calificacion {i}: "))
                if cal >= 0 and cal <= 11:
                    calificaciones.append(cal)
                    continuar = False
                else:
                    print("\033[91m Error \u274C : Ingresa una calificacion correcta\033[0m")
            except ValueError:
                print("\033[91m Error \u274C : Ingresa un valor numerico valido\033[0m")
    lista.append([nombre]+calificaciones)
    print("\033[92mAccion realizada con éxito \U0001F44D\033[0m")
    esperarTecla()

def mostrar_calificacion(lista):
    borrarPantalla()
    print("Mostrar calificaciones: \U0001F4C2 ")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calf 1':<10}{'Calf 2':<10}{'Calf 3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print(f"{'-'*40}")
            cuantos=len(lista)
            print(f"\033[92m Son {cuantos} estudiantes en el sistema\033[0m")
    else:
        print("\033[91m No hay calificaciones registradas en el sistema \u274C\033[0m")
    esperarTecla() 

def calcular_promedio(lista):
    borrarPantalla()
    print("Calcular promedio: \U0001F4DD ")
    if len(lista)>0:
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{'Nombre':<15}{'Promedio':<10}")
            print(f"{'-'*25}")
            print(f"{nombre:<15}{promedio:.2f}")
    else:
        print("\033[91m No hay calificaciones registradas en el sistema \u274C\033[0m")

    esperarTecla()

