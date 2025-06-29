'''crear un proyecto que permita gestionar calificaciones, colocar un menu de opciones para agragar, mostrar, calcular promedio calificaciones de un estudiantes

notas: utlizar funciones y mandar llamar desde otro archivo (modulo)
utilizar un lista bidimensional para alamacenar el nombre del estudiante y sus tres calificaciones'''

import calificaciones




def main():
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":

               calificaciones.anadir_calificacion(datos)

            case "2":
                calificaciones.mostrar_calificacion(datos)

            case "3":
                calificaciones.calcular_promedio(datos)

            case "4":
                opcion=False
                calificaciones.borrarPantalla()    
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")



if __name__ == "__main__":
    main()