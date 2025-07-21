
import agenda


def main():
    agenda_contactos = {}

    opcion=True
    while opcion:
        agenda.borrar_pantalla()
        opcion=agenda.menu_principal()

        match opcion:
            case 1:
                agenda.agregar_contacto(agenda_contactos)
            case 2:
                agenda.mostrar_contactos(agenda_contactos)
            case 3:
                agenda.buscar_contacto(agenda_contactos)
            case 4:
                agenda.modificar_contacto(agenda_contactos)
            case 5:
                agenda.eliminar_contacto(agenda_contactos)
            case 6:
                print("👋 Cerrando sistema.")
                break
            case _:
                print("⚠️ Opción inválida. Intenta de nuevo.")
                agenda.esperar_tecla()


if __name__ == "__main__":
    main()
