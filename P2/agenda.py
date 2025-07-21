agenda=( "EDDIE", "61811345678", "eddie312456789@gmail.com"
                    "SEBASTIAN", "61878945613", "sebastian8859854@gmail.com",
                    "DIEGO", "61894561237", "diego212547652@gmail.com" 
                    )                  


def borrarPantalla():
    import os

def esperar_tecla():
    input("🔷 Presiona una tecla para continuar...")


def menu_principal():
    while True:
        borrarPantalla()
        print("...::: Sistema de Gestion de Agenda de Contactos :::...")
        print("1️⃣    Agregar contacto")
        print("2️⃣    Mostrar todos los contactos")
        print("3️⃣    Buscar contacto por nombre")
        print("4️⃣    Modificar contacto")
        print("5️⃣    SALIR")

        opcion = input("🔷 Elige una opcion (1-4): ")


def modificar_contactos(agenda):
    borrarpantalla()
    print("\n\t\t \U0001F501 .::Modificar Contactos::. \U0001F501")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        nom=input("Ingresa el nombre del contacto que desea modificar: ").upper().strip()
        encontro=0
        for nombre,datos in agenda.items():
            if nombre==nom:
                print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
                tel=input("Ingrese el nuevo numero de telefono: ")
                mail=input("Ingrese el nuevo e-mail: ")
                datos[0]=tel
                datos[1]=mail
                encontro+=1
        if encontro==0:
            print(f"\n\t \u274C No se encontro un contacto con el nombre {nom} para modificar \u274C")

       
        
def eliminar_contacto(agenda):
    borrarpantalla()
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