from paquete1 import modulos

print(modulos.saludar("Eduardo Chavez Guerrero"))

modulos.borrarPantalla()

nombre, telefono=modulos.solicitar_datos2()
print(f"\n\t Agenda telefonica\n\t\n \t Nombre: {nombre}\n\t Telefono: {telefono}")

modulos.esperarTecla()
