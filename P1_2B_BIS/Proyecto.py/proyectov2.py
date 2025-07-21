# 🥂🍸 Sistema de Inventario y Administración de Empleados para Barman 🍹🍷

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
        else:
            print("⚠️ Solo se permite 'bebida' o 'licor'. Intenta de nuevo.")
    
    while True:
        try:
            cantidad = int(input("🔹 Cantidad en stock: "))
            if cantidad >= 0:
                break
            else:
                print("⚠️ Ingresa un número positivo.")
        except ValueError:
            print("⚠️ Solo se permiten números enteros.")
    
    while True:
        try:
            precio = float(input("🔹 Precio unitario ($): "))
            if precio >= 0:
                break
            else:
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

def menu_principal():
    while True:
        borrar_pantalla()
        print("🍽️ =============================== 🍽️")
        print("   Sistema de Barman - Restaurante")
        print("🍽️ =============================== 🍽️")
        print("1. ➕ Agregar producto al inventario")
        print("2. 📋 Mostrar inventario")
        print("3. 👤 Agregar empleado")
        print("4. 👥 Mostrar empleados")
        print("5. 🚪 Salir")
        
        opcion = input("🔷 Selecciona una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            agregar_empleado()
        elif opcion == "4":
            mostrar_empleados()
        elif opcion == "5":
            print("👋 Cerrando sistema. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")
            esperar_tecla()

# Ejecutar menú principal
menu_principal()
