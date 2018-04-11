
#creo e inicializo las variables
edad 		=0
var_nombre	=""
#preguntamos la edad
edad= int(input("dime tu edad:\n"))
#comprobamos si el usuario es mayor o menor de edad
if edad >17:
	var_nombre = input("introduce tu nombre:\n")
	print("hola", var_nombre)
else:
	print("Este programa es solo para mayores de edad")
#siempre nos despedimos
print("Hasta pronto")