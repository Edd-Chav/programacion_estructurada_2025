peliculas=[]

def borrarPantalla():
  import os  
  os.system("clear")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ")
  peliculas.append(input("Ingresa el nombre: ").upper().strip)
  input("\n\t\t     LA OPERACION SE REALIZO CON EXIGO   ")

def consultarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consultar Peliculas ::.")
if len(peliculas):
  for i in range (0, len, peliculas):
    print(f"{i+1} {peliculas[1]}")
else:
  print("\t .:: No hay peliculas en el sistema ::.")

