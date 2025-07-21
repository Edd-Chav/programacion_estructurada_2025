'''hacer un sistema de gestion de agenda de contactos con listas dentro de un diccionario, que permita agregar, mostrar y buscar contactos por nombre.'''
contactos_agenda = {}

def borrar_pantalla():
    import os
    os.system("cls")

def esperar_tecla():
    input("🔷 Presiona Enter para continuar...")

def menu_principal():
        borrar_pantalla()
        print(" =============================== ")
        print("   Sistema de Gestión de Agenda")
        print(" =============================== ")
        print("1. ➕ Agregar contacto")
        print("2. 📋 Mostrar contactos")
        print("3. 🗑️ Buscar contacto por nombre")
        print("4. 🚪 Modificar Contacto")
        print("5.   Eliminar Contacto")
        print("6. 👋 Salir")

        opcion = int(input("🔷 Selecciona una opción: "))
        return opcion
        

def agregar_contacto(agenda):
    
    borrar_pantalla()
    print("➕ .:: Agregar Contacto ::. ➕")
    
    nombre = input("🔷 Ingresa el nombre del contacto: ").upper().strip()
    if nombre in contactos_agenda:
        print("⚠️ El contacto ya existe...")
    else:
         tel= input("🔷 Ingresa el número de teléfono: ").strip()
         correo= input("🔷 Ingresa el correo electrónico: ").strip().lower()
         agenda[nombre]=[tel, correo]
         print(f"✅ Contacto {nombre} agregado exitosamente.")
         esperar_tecla()
         
        

def mostrar_contactos(agenda):
    borrar_pantalla()
    print("🔍 .:: Buscar Contacto ::. 🔍")
    if not agenda:
        print("⚠️ No hay contactos en la agenda.")
    else:
         for nombre,datos in agenda.items():
            print(f"🔷 Nombre: {nombre}")
            print(f"   📞 Teléfono: {datos[0]}")
            print(f"   📧 Correo: {datos[1]}")
            print("📅 ----------------------------- 📅")
    esperar_tecla()

def buscar_contacto(agenda):
    borrar_pantalla()
    print("🔍 .:: Buscar Contacto ::. 🔍")
    
    nombre = input("🔷 Ingresa el nombre del contacto a buscar: ").upper().strip()
    
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"🔷 Nombre: {nombre}")
        print(f"   📞 Teléfono: {datos[0]}")
        print(f"   📧 Correo: {datos[1]}")
    else:
        print("⚠️ Contacto no encontrado.")
    
    esperar_tecla()

def modificar_contacto(agenda):
    borrar_pantalla()
    print("✏️ .:: Modificar Contacto ::. ✏️")
    
    nombre = input("🔷 Ingresa el nombre del contacto a modificar: ").upper().strip()
    
    if nombre in agenda:
        tel = input("🔷 Ingresa el nuevo número de teléfono: ").strip()
        correo = input("🔷 Ingresa el nuevo correo electrónico: ").strip().lower()
        agenda[nombre] = [tel, correo]
        print(f"✅ Contacto {nombre} modificado exitosamente.")
    else:
        print("⚠️ Contacto no encontrado.")
    
    esperar_tecla()

def modificar_contacto(agenda):
    borrar_pantalla()
    print(" .:: Modificar Contacto ::. ")

    nombre = input(" Ingresa el nombre del contacto a modificar: ").upper().strip()
    
    if nombre in agenda:
        tel = input("🔷 Ingresa el nuevo número de teléfono: ").strip()
        correo = input("🔷 Ingresa el nuevo correo electrónico: ").strip().lower()
        agenda[nombre] = [tel, correo]
        print(f"✅ Contacto {nombre} modificado exitosamente.")
    else:
        print("⚠️ Contacto no encontrado.")
    
    esperar_tecla()


def eliminar_contacto(agenda):
    borrar_pantalla()
    encontro = 0
    conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
    confirmar = ""
    for nombre, datos in agenda.items():
        if nombre == conta_eliminar:
            print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:' + datos[0]}\n\t{'E-mail:' + datos[1]}")
            while confirmar != "si" and confirmar != "no":
                confirmar = input("¿Estás seguro que deseas eliminar este contacto? (Si/No): ").lower().strip()
                if confirmar != "si" and confirmar != "no":
                    print("\n\t\t \u274C Respuesta inválida. Por favor escribe 'Si' o 'No' \u274C")
            if confirmar == "si":
                agenda.pop(nombre)
                print(f"\n\t \u2705 El contacto '{nombre}' ha sido eliminado exitosamente. \u2705")
                encontro += 1
    if encontro == 0:
        print(f"\n\t \u274C No se encontró un contacto con el nombre {conta_eliminar} \u274C")
    esperar_tecla()