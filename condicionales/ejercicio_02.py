#Pedir un numero y decir si es positivo, negativo o 0

numero = int(input('ingresa un numero: '))
if numero == 0:
	print('el numero es cero')
else:
	if numero > 0:
		print('el numero es positivo')
	else:
		print('el numero es negativo')