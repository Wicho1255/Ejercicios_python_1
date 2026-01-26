#Estructura de control if
# if else elif

'''
if exp_booleana:
	intrucciones

if expo_booleana:
	instrucciones
else:
	instrucciones

if exp:bool:
	instrucciones
elif exp_bool:
	intrucciones
else:
	intrucciones
'''

numero = int(input('escribe un numero:'))

if numero > 0:
	print("es un numero positivo")
elif numero == 0:
	print('El numero es 0')
else:
	print('es un numero negativo')