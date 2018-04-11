#Fijar las variables y establecer sus valores
numeropar =0
multiprodetres=0
menu = "si"
#Pedir un numero al usuario para decir si es par o impar o multipro de 3
while menu=="si"
	numeropar= int(input("Dime un numero y te dire si es par o impar o multiplro de 3 \n"))
	multiprodetres=numeropar
	if numeropar %2 == 0:
		print("Es un numero par")
	else:
		print("Es un numero impar")
	if multiprodetres %3 ==0:
		print("Es un multiplo de tres")
	menu = int(input("¿Quieres saber otro numero? (s/n)\n"))
	if menu!= "si"
		print("Nos vemos cuandos quieras aprender mas")