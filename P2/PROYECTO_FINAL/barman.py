# barman.py

inventario = []
empleados = []

def borrar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("🔷 Presiona ENTER para continuar...")

def agregar_producto():
    borrar_pantalla()
    print("🍾 .:: Agregar Producto al Inventario ::. 🍾")
    nombre = input("🔹 Nombre del producto: ").strip()

    while True:
        tipo = input("🔹 Tipo (bebida/licor): ").strip().lower()
        if tipo in ["bebida", "licor"]:
            break
        print("⚠️ Solo se permite 'bebida' o 'licor'. Intenta de nuevo.")

    while True:
        try:
            cantidad = int(input("🔹 Cantidad en stock: "))
            if cantidad >= 0:
                break
            print("⚠️ Ingresa un número positivo.")
        except ValueError:
            print("⚠️ Solo se permiten números enteros.")

    while True:
        try:
            precio = float(input("🔹 Precio unitario ($): "))
            if precio >= 0:
                break
            print("⚠️ Ingresa un número positivo.")
        except ValueError:
            print("⚠️ Solo se permiten números (ejemplo: 25.50).")

    producto = {
        "nombre": nombre,
        "tipo": tipo,
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(producto)
    print("✅ Producto agregado exitosamente.")
    esperar_tecla()

def mostrar_inventario():
    borrar_pantalla()
    print("📦 .:: Inventario de Bebidas y Licores ::. 📦")
    if not inventario:
        print("⚠️ No hay productos en el inventario.")
    else:
        for i, p in enumerate(inventario, start=1):
            print(f"{i}. 📝 Nombre: {p['nombre']} | 🍹 Tipo: {p['tipo']} | 🔢 Cantidad: {p['cantidad']} | 💲 Precio: ${p['precio']:.2f}")
    esperar_tecla()

def eliminar_producto():
    borrar_pantalla()
    print("🗑️ .:: Eliminar Producto del Inventario ::. 🗑️")
    if not inventario:
        print("⚠️ No hay productos para eliminar.")
    else:
        print("📋 Productos disponibles:")
        for i, p in enumerate(inventario, start=1):
            print(f"{i}. 📝 Nombre: {p['nombre']} | 🍹 Tipo: {p['tipo']} | 🔢 Cantidad: {p['cantidad']} | 💲 Precio: ${p['precio']:.2f}")
        try:
            opcion = int(input("🔷 Ingresa el número del producto a eliminar: "))
            if 1 <= opcion <= len(inventario):
                eliminado = inventario.pop(opcion - 1)
                print("✅ Producto eliminado:")
                print(f"📝 Nombre: {eliminado['nombre']} | 🍹 Tipo: {eliminado['tipo']} | 🔢 Cantidad: {eliminado['cantidad']} | 💲 Precio: ${eliminado['precio']:.2f}")
            else:
                print("⚠️ Opción fuera de rango.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")
    esperar_tecla()

def agregar_empleado():
    borrar_pantalla()
    print("👨‍🍳 .:: Agregar Empleado ::. 👩‍🍳")
    nombre = input("🔹 Nombre del empleado: ").strip()
    puesto = input("🔹 Puesto: ").strip()

    empleado = {
        "nombre": nombre,
        "puesto": puesto
    }
    empleados.append(empleado)
    print("✅ Empleado agregado exitosamente.")
    esperar_tecla()

def mostrar_empleados():
    borrar_pantalla()
    print("👥 .:: Lista de Empleados ::. 👥")
    if not empleados:
        print("⚠️ No hay empleados registrados.")
    else:
        for i, e in enumerate(empleados, start=1):
            print(f"{i}. 📝 Nombre: {e['nombre']} | 💼 Puesto: {e['puesto']}")
    esperar_tecla()

def eliminar_empleado():
    borrar_pantalla()
    print("🗑️ .:: Eliminar Empleado ::. 🗑️")
    if not empleados:
        print("⚠️ No hay empleados para eliminar.")
    else:
        print("📋 Empleados registrados:")
        for i, e in enumerate(empleados, start=1):
            print(f"{i}. 📝 Nombre: {e['nombre']} | 💼 Puesto: {e['puesto']}")
        try:
            opcion = int(input("🔷 Ingresa el número del empleado a eliminar: "))
            if 1 <= opcion <= len(empleados):
                eliminado = empleados.pop(opcion - 1)
                print("✅ Empleado eliminado:")
                print(f"📝 Nombre: {eliminado['nombre']} | 💼 Puesto: {eliminado['puesto']}")
            else:
                print("⚠️ Opción fuera de rango.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")
    esperar_tecla()

def menu_principal():
    while True:
        borrar_pantalla()
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

