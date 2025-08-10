import mysql.connector

def obtener_conexion_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="barman"
        )
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def inicializar_bd():
    conn = obtener_conexion_bd()
    if conn is None:
        print("No se pudo conectar a la base de datos para inicializar.")
        return
    cursor = conn.cursor()
    # Crea la tabla empleados si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(50) UNIQUE NOT NULL,
            contrasena VARCHAR(50) NOT NULL
        )
    """)
    # Crea la tabla productos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10,2) NOT NULL
        )
                   
    """)
    conn.commit()
    cursor.close()
    conn.close()