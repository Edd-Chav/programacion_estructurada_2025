# 1er forma de utilizar los modulos
import modulos

#modulos.borrarPantalla()
print(modulos.saludar("Sebastian"))

# 2da forma de utilizar los modulos
from modulos import saludar, borrarPantalla
print(saludar("Sebastian"))
#borrarPantalla()


nombre= input("ingresa el nombre:")
telefono= input("ingresa el telefono:")
nombre, telefono = modulos.solicitar_datos4(nombre, telefono)
print (f"\tnombre: {nombre} \n\t telefono: {telefono}")
