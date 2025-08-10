from conexionBD import inicializar_bd
from funciones import limpiar_pantalla
from empleados.empleado import registrar_empleado, iniciar_sesion
from inventarios.inventario import agregar_producto, mostrar_inventario, eliminar_producto, modificar_producto

def menu_inicio():
    while True:
        limpiar_pantalla()
        print("🍸\t\t=== SISTEMA BARMAN ===")
        print("\n\t1️⃣\tRegistrarse")
        print("\t2️⃣\tIniciar sesión")
        print("\t3️⃣\tSalir")
        opcion = input("\n👉\tSelecciona: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            if iniciar_sesion():
                menu_inventario()
        elif opcion == "3":
            print("\n👋✨\t¡Hasta pronto! Gracias por usar el programa. 🥂")
            break
        else:
            input("❌\tOpción inválida, presiona cualquier tecla para continuar...")

def menu_inventario():
    while True:
        limpiar_pantalla()
        print("📦\t\t=== MENÚ INVENTARIO ===")
        print("\n\t1️⃣\tAñadir producto")
        print("\t2️⃣\tMostrar inventario")
        print("\t3️⃣\tEliminar producto")
        print("\t4️⃣\tModificar producto")
        print("\t5️⃣\tCerrar sesión")
        opcion = input("\n👉\tSelecciona: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            print("\n🔒👋\tCerrando la sesión... Volviendo al menú principal. 🏠")
            from funciones import esperar_tecla
            esperar_tecla()
            break
        else:
            input("❌\tOpción inválida. Presiona ENTER...")

if __name__ == "__main__":
    inicializar_bd()  
    menu_inicio()