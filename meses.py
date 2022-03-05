#Ejemplo de meses del año

mes = input("Digite mes del año")
print(f"El mes digitado fue {mes}")

#Caminos para clasificar el mes
if(mes == "Diciembre" or mes == "Enero" or mes == "Febrero" or mes == "Marzo"):
    print("Estas en Invierno")
elif(mes == "Junio" or mes == "Julio" or mes == "Agosto"):
    print("Estas en Verano")
elif(mes == "Abril" or mes == "Mayo"):
    print("Estas en Primavera")
elif(mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre"):
    print("Estamos en Otoño")