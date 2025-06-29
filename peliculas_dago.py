import os
os.system("cls")

peliculas=[]
pelicula={}

'''diccionario de peliculas con caracteristicas nombre categoria clasificacion genero idioma'''

def borrarPantalla():
      os.system("cls")

def esperarTecla():
        input("Presiona una tecla para continuar...")

def anadir_peliculas():
    print("\n\t ..::: AÑADIR PELICULAS :::...\n")
    pelicula.update({
        "nombre": input("Ingrese el nombre de la pelicula: ").upper().strip(),})
    pelicula.update({
        "categoria": input("Ingrese la categoria de la pelicula: ").upper().strip(),})
    pelicula.update({
        "clasificacion": input("Ingrese la clasificacion de la pelicula: ").upper().strip(),})
    pelicula.update({
        "genero": input("Ingrese el genero de la pelicula: ").upper().strip(),})
    pelicula.update({
        "idioma": input("Ingrese el idioma de la pelicula: ").upper().strip(),})
    
def consultar_peliculas():
    borrarPantalla()
    print("consultar peliculas")
    if len(peliculas) > 0:
        print("Lista de peliculas:")
        for pelicula in peliculas:
            print(f"- {pelicula}")

def vaciar_peliculas():
    borrarPantalla()
    print("\n\t ..::: VACIAR PELICULAS :::...\n")
    resp=input("Deseas borrar todas las peliculas? (S/N)").upper()
    if resp == "S":
        peliculas.clear()
        print("Todas las peliculas han sido eliminadas.")
    else:
        print("No se han eliminado peliculas.")
    esperarTecla()

def buscar_peliculas():
    borrarPantalla()
    print("\n\t ..::: BUSCAR PELICULAS :::...\n")
    peliculas_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0

    if not peliculas_buscar in peliculas:
         print("No se ha ingresado un nombre de pelicula.")
    else:
          for i in range(0, len(peliculas)):
               if peliculas_buscar == peliculas[i]:
                    print(f"la pelicula {peliculas_buscar} se encuentra en la lista y esta en la pocision {i+1}")
                    encontro+=1
               if encontro>0:
                print(f"La pelicula {peliculas_buscar} se encuentra {encontro} veces en la lista")

def borrar_pelicula():
    borrarPantalla()
    print("\n\t ..::: BORRAR PELICULA :::...\n")
    pelicula_borrar=input("Ingrese el nombre de la pelicula a eliminar: ").upper().strip()
    encontro = 0
    if not pelicula_borrar in peliculas:
        print("No se ha ingresado un nombre de pelicula.")
    else:
        for i in range(0, len(peliculas)):
            if pelicula_borrar == peliculas[i]:
                print(f"La pelicula {pelicula_borrar} se encuentra en la lista y esta en la posicion {i+1}")
                encontro += 1
        if encontro > 0:
            peliculas.remove(pelicula_borrar)
            print(f"La pelicula estaba en la posicion {i+1} y ha sido eliminada.")
            

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t .:: Agregar Caracteristica a Peliculas ::.\n")
    atributo=input("Ingresa la nueva caracteristica de la Pelicula: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    pelicula.update({atributo:valor})

def modificarCaracteristicasPeliculas():
    borrarPantalla
    print("\n\t .::Modificar caracteristica a peliculas::.\n")
    atributo = input("\n¿Qué atributo deseas modificar? (nombre, categoria, clasificacion, genero, idioma): ").lower().strip()
    if atributo in pelicula:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ").upper().strip()
        pelicula[atributo] = nuevo_valor
        print(f"\n\tSe ha actualizado '{atributo}' a: {nuevo_valor}")
    else:
        print("\n\tEl atributo ingresado no es válido.")

def borrarCaracteristicas():
    borrarPantalla()
    print("\n\t .::Modificar caracteristica a peliculas::.\n")
    atributo = input("Ingresa la caracteristica que deseas modificar: ").lower().strip()
    if atributo in pelicula:
        nuevo_valor = input("Ingresa el nuevo valor de la caracteristica: ").upper().strip()
        pelicula.update({atributo: nuevo_valor})
        print("\n\t ::: Caracteristica modificada con exito! :::")
    else:
        print("\n\t La caracteristica no existe.")
    input("\n\t Oprima cualquier tecla para continuar...")



def eliminarPeliculas():
   borrarPantalla()
   print("\n\t.:: Borrar Películas ::.\n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in pelicula): 
      print("\n\t\t ¡No se encuentra la pelicula a buscar!")   
   else: 
      resp="si"  
      while pelicula_buscar in peliculas and resp=="si":
          resp=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No)?").lower()
          if resp=="si":
            posicion=peliculas.index(pelicula_buscar)
            print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
            peliculas.remove(pelicula_buscar) 
            encontro+=1
            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      print(f"Se borro {encontro} pelicula(s) con este titulo")
                    




    