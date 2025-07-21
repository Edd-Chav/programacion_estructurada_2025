# main.py

import barman
from barman import agregar_producto, mostrar_inventario, eliminar_producto, agregar_empleado, mostrar_empleados, eliminar_empleado, esperar_tecla, borrar_pantalla
import os

def menu_principal():
    while True:
        os.system("cls")
        print("🍽️ =============================== 🍽️")
        print("   Sistema de Barman - Restaurante")
        print("🍽️ =============================== 🍽️")
        print("1. ➕ Agregar producto al inventario")
        print("2. 📋 Mostrar inventario")
        print("3. 🗑️ Eliminar producto del inventario")
        print("4. 👤 Agregar empleado")
        print("5. 👥 Mostrar empleados")
        print("6. 🗑️ Eliminar empleado")
        print("7. 🚪 Salir")
        
        opcion = input("🔷 Selecciona una opción: ")

        match opcion:
            case "1":
                agregar_producto()
            case "2":
                mostrar_inventario()
            case "3":
                eliminar_producto()
            case "4":
                agregar_empleado()
            case "5":
                mostrar_empleados()
            case "6":
                eliminar_empleado()
            case "7":
                print("👋 Cerrando sistema. ¡Hasta luego!")
                break
            case _:
                print("⚠️ Opción inválida. Intenta de nuevo.")
                esperar_tecla()

if __name__ == "__main__":
    menu_principal()
    print("👋 Gracias por usar el sistema de Barman. ¡Hasta luego!")

