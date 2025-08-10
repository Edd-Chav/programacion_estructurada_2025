import getpass
from conexionBD import obtener_conexion_bd
from funciones import limpiar_pantalla, esperar_tecla

def registrar_empleado():
    limpiar_pantalla()
    print("=== REGISTRAR EMPLEADO ===")
    usuario = input("Usuario: ")
    contrasena = getpass.getpass("Contraseña: ")

    conn = obtener_conexion_bd()
    if conn is None:
        print("❌ No se pudo conectar a la base de datos.")
        esperar_tecla()
        return

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO empleados (usuario, contrasena) VALUES (%s, %s)", (usuario, contrasena))
        conn.commit()
        print("✅ Registro exitoso.")
    except Exception as e:
        print(f"❌ Error: {e}")
    cursor.close()
    conn.close()
    esperar_tecla()

def iniciar_sesion():
    limpiar_pantalla()
    print("=== INICIAR SESIÓN ===")
    usuario = input("Usuario: ")
    contrasena = getpass.getpass("Contraseña: ")

    conn = obtener_conexion_bd()
    if conn is None:
        print("❌ No se pudo conectar a la base de datos.")
        esperar_tecla()
        return False

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE usuario=%s AND contrasena=%s", (usuario, contrasena))
    empleado = cursor.fetchone()
    cursor.close()
    conn.close()

    if empleado:
        print("✅ Inicio de sesión exitoso.")
        esperar_tecla()
        return True
    else:
        print("❌ Usuario o contraseña incorrectos.")
        esperar_tecla()
        return False