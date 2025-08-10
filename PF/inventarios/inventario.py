from conexionBD import obtener_conexion_bd
from funciones import limpiar_pantalla, esperar_tecla

def agregar_producto():
    limpiar_pantalla()
    print("➕\t\t=== AÑADIR PRODUCTO ===")
    nombre = input("📝\tNombre: ").strip()
    if not nombre:
        print("❌\tEl nombre no puede estar vacío.")
        esperar_tecla()
        return
    while True:
        cantidad_str = input("🔢\tCantidad: ")
        try:
            cantidad = int(cantidad_str)
            break
        except ValueError:
            print("❌\tSolo puedes ingresar números enteros para la cantidad. Intenta de nuevo.")
    while True:
        precio_str = input("💲\tPrecio: ")
        try:
            precio = float(precio_str)
            break
        except ValueError:
            print("❌\tSolo puedes ingresar números para el precio. Intenta de nuevo.")

    while True:
        tipo = input("🍾\tTipo (licor/bebida): ").strip().lower()
        if tipo in ("licor", "bebida"):
            break
        print("⚠️\tDebes ingresar solo 'licor' o 'bebida'. Intenta de nuevo.")

    conn = obtener_conexion_bd()
    if conn is None:
        print("❌\tNo se pudo conectar a la base de datos.")
        esperar_tecla()
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO inventario (nombre, cantidad, precio, tipo) VALUES (%s, %s, %s, %s)",
            (nombre, cantidad, precio, tipo)
        )
        conn.commit()
        print("✅\tProducto añadido correctamente.")
    except Exception as e:
        print(f"❌\tError al añadir producto: {e}")
    cursor.close()
    conn.close()
    esperar_tecla()

def mostrar_inventario():
    limpiar_pantalla()
    print("📋\t\t=== INVENTARIO ===")
    conn = obtener_conexion_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventario")
    productos = cursor.fetchall()
    print("\n🗂️  {0:<4} | {1:<18} | {2:<8} | {3:<10} | {4:<8}".format(
        "ID", "🏷️ Nombre", "🔢 Cant.", "💲 Precio", "🍾 Tipo"))
    print("   " + "-"*60)
    for p in productos:
        nombre = (p[1][:16] + '…') if len(p[1]) > 17 else p[1]
        print("   {0:<4} | {1:<18} | {2:<8} | ${3:<9.2f} | {4:<8}".format(
            p[0], nombre, p[2], p[3], p[4]))
    cursor.close()
    conn.close()
    esperar_tecla()
    
def eliminar_producto():
    limpiar_pantalla()
    print("🗑️\t\t=== ELIMINAR PRODUCTO ===")
    conn = obtener_conexion_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, cantidad, precio, tipo FROM inventario")
    productos = cursor.fetchall()
    if not productos:
        print("⚠️\tNo hay productos para eliminar.")
        cursor.close()
        conn.close()
        esperar_tecla()
        return

    print("\n🗂️  {0:<4} | {1:<18} | {2:<8} | {3:<10} | {4:<8}".format(
        "ID", "🏷️ Nombre", "🔢 Cant.", "💲 Precio", "🍾 Tipo"))
    print("   " + "-"*60)
    for p in productos:
        nombre = (p[1][:16] + '…') if len(p[1]) > 17 else p[1]
        print("   {0:<4} | {1:<18} | {2:<8} | ${3:<9.2f} | {4:<8}".format(
            p[0], nombre, p[2], p[3], p[4]))

    while True:
        opcion = input("\n❓\t¿Deseas eliminar un producto? (si/no): ").strip().lower()
        if opcion in ("si", "no"):
            break
        print("⚠️\tSolo puedes ingresar 'si' o 'no'. Intenta de nuevo.")
    if opcion == "no":
        print("⏪\tEliminación cancelada. Regresando al menú...")
        esperar_tecla()
        cursor.close()
        conn.close()
        return

    while True:
        id_str = input("🗂️\tIngresa el ID del producto a eliminar: ")
        try:
            id_prod = int(id_str)
            break
        except ValueError:
            print("❌\tSolo puedes ingresar números para el ID. Intenta de nuevo.")

    cursor.execute("SELECT nombre FROM inventario WHERE id=%s", (id_prod,))
    prod = cursor.fetchone()
    if not prod:
        print("❌\tNo existe un producto con ese ID.")
        cursor.close()
        conn.close()
        esperar_tecla()
        return

    while True:
        confirmar = input(f"❓\t¿Seguro que deseas eliminar '{prod[0]}'? (si/no): ").strip().lower()
        if confirmar == "si":
            cursor.execute("DELETE FROM inventario WHERE id=%s", (id_prod,))
            conn.commit()
            print("✅\tProducto eliminado correctamente.")
            break
        elif confirmar == "no":
            print("⏪\tEliminación cancelada. Regresando al menú...")
            break
        else:
            print("⚠️\tSolo puedes ingresar 'si' o 'no'. Intenta de nuevo.")

    cursor.close()
    conn.close()
    esperar_tecla()

def modificar_producto():
    while True:
        limpiar_pantalla()
        print("✏️\t\t=== MODIFICAR PRODUCTO ===")
        conn = obtener_conexion_bd()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventario")
        productos = cursor.fetchall()

        if not productos:
            print("⚠️\tNo hay productos para modificar.")
            cursor.close()
            conn.close()
            esperar_tecla()
            return

        print("\n🗂️  {0:<4} | {1:<18} | {2:<8} | {3:<10} | {4:<8}".format(
            "No.", "🏷️ Nombre", "🔢 Cant.", "💲 Precio", "🍾 Tipo"))
        print("   " + "-"*60)
        for i, p in enumerate(productos, start=1):
            nombre = (p[1][:16] + '…') if len(p[1]) > 17 else p[1]
            print("   {0:<4} | {1:<18} | {2:<8} | ${3:<9.2f} | {4:<8}".format(
                i, nombre, p[2], p[3], p[4]))

        while True:
            opcion = input("\n❓\t¿Deseas modificar un producto? (si/no): ").strip().lower()
            if opcion in ("si", "no"):
                break
            print("⚠️\tSolo puedes ingresar 'si' o 'no'. Intenta de nuevo.")
        if opcion == "no":
            print("⏪\tModificación cancelada. Regresando al menú...")
            esperar_tecla()
            cursor.close()
            conn.close()
            return

        while True:
            num_str = input("🔢\tIngresa el número del producto a modificar: ")
            try:
                num = int(num_str)
                break
            except ValueError:
                print("❌\tSolo puedes ingresar números para el número de producto. Intenta de nuevo.")

        cursor.execute("SELECT id FROM inventario")
        ids = cursor.fetchall()

        if 1 <= num <= len(ids):
            nombre = input("📝\tNuevo nombre: ").strip()
            while True:
                cantidad_str = input("🔢\tNueva cantidad: ")
                try:
                    cantidad = int(cantidad_str)
                    break
                except ValueError:
                    print("❌\tSolo puedes ingresar números enteros para la cantidad. Intenta de nuevo.")
            while True:
                precio_str = input("💲\tNuevo precio: ")
                try:
                    precio = float(precio_str)
                    break
                except ValueError:
                    print("❌\tSolo puedes ingresar números para el precio. Intenta de nuevo.")
            while True:
                tipo = input("🍾\tNuevo tipo (licor/bebida): ").strip().lower()
                if tipo in ("licor", "bebida"):
                    break
                print("⚠️\tDebes ingresar solo 'licor' o 'bebida'. Intenta de nuevo.")

            cursor.execute(
                "UPDATE inventario SET nombre=%s, cantidad=%s, precio=%s, tipo=%s WHERE id=%s",
                (nombre, cantidad, precio, tipo, ids[num - 1][0])
            )
            conn.commit()
            print("✅\tProducto modificado.")
        else:
            print("❌\tNúmero inválido.")

        cursor.close()
        conn.close()
        esperar_tecla()
        break