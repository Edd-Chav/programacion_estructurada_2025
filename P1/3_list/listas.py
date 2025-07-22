import os
numeros= [10,9,8,7,6,6,5,4,3,2,1,0]
numeros.sort()
print(numeros)

for i in numeros:
    print(i)


for i in range(0,len(numeros)):
    print(numeros[i])

    os.system("cls")

    #utencilios_cocina = ["Cuchara", "Tenedor", "Cuchillo", "Plato", "Vaso"]
    #print(utencilios_cocina)

#1era forma
    #utencilios_cocina_buscar=input("Dame el utensilio a buscar: ")
    #for i in range(0, len(utencilios_cocina)):
        #if utencilios_cocina[i] == utencilios_cocina_buscar:
            #print(f"el utencilio de cocina {utencilios_cocina_buscar} si existe")
        #else:
            #print(f"el utencilio de cocina {utencilios_cocina_buscar} no existe")

#2da forma
    #utencilios_cocina_buscar=input("Dame el utensilio a buscar: ")
    #print(f"el numero de veces que se encontro la palabra es: {utencilios_cocina.count(utencilios_cocina_buscar)}")
    #if utencilios_cocina_buscar in utencilios_cocina:
        #print(f"el utencilio de cocina si existe")
    #else:
        #print(f"el utencilio de cocina no existe")
    
#3ra forma
    #utencilios_cocina_buscar=input("Dame el utensilio a buscar: ")
    #encontro=False
    #for i in range(0, len(utencilios_cocina)):
        #if utencilios_cocina[i] == utencilios_cocina_buscar:
            #encontro=True
    #if encontro:
       #print(F"SI SE ENCONTRO")
    #else:
        #print(F"NO SE ENCONTRO")


    

    

    #Añadir elementos a una lista
#    os.system("cls")
 #   numeros= [10,9,8,7,6,6,5,4,3,2,1,0]
  #  numeros.sort()
   # print(numeros)

    #numeros=[]
    #opc=True
    #while opc:
    #    numeros=float(input("dame un numero:"))
    #    numeros.append(numeros)
    #resp= input("¿Deseas seguir ingresando numeros? (s/n): ").lower()
    #if resp == 's':
     #   opc = True
    #else:
     #   opc = False

    #print(numeros)
    #input("Presiona una tecla para continuar...")

    #crear una lista multidimensional que sea una agenda

    
    agenda = [
        ["Sebastian", "618959824"],
        ["Diego", "6187487557"],
        ["Eddie", "6182872744"],
             ]
    
    cadena=""
    for r in range(0,3):
        for c in range(0,2):
            cadena +=f"{agenda[r][c]} "
            cadena += "\n"
            print(cadena)
