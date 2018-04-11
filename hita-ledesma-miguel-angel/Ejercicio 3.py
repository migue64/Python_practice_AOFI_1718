var_numero = 0
var_numero = 0
var_numero = 0

print("Dime un numero mayor que 0")
var_numero1 = ont(input())
if var_numero > 0:
	print("Dime un numero mayo que el anterior")
	var_numero2 = int(input())
	if var_numero2 > var_numero1:
		print("Un numero mayor que 0")
		var_numero3 = int(input())
		if var_numero3 < 0:
			print (var_numero1, "+", var_numero2, "+", var_numero3, "=", var_numero1+var_numero2+var_numero3)