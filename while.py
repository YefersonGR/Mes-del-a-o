#Variable controladora
import imp


numero=1

#Declaro el bucle/ciclo/iteración/repeticion/la vuelta/loop
while(numero<=20):
    print("Abrase")
    print(numero)
    numero+=1



#Importar libreria (Recetas,codigos prefabricados)
import math

print("Empanadas el machetico")
print("***")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raíz cuadrada de un #")
print("2. Digita 2 para calcular la potencia de 2 de un #")
print("***")

opcion=1

while(opcion!=0):   

    #Variable controladora

    #Pregunte por la opción
    opcion=int(input("Digita la opcion"))

    
    if(opcion==1):
        numero=int(input("Digita un número"))
        raiz=math.sqrt(numero)
        print(f"La raíz de {numero} es {raiz}")
    elif(opcion==2):
        numero=int(input("Digita un número"))
        potencia=math.pow(numero,2)
        print(f"La potencia del número es {potencia}")
    else:
        print("Digita un número valido ome")


    