# programa que hace una diivison
#si el divisor es 0 que termine o que diga que no se puede

num_1 = int(input('ingresa un numero: '))
num_2 = int(input('ingresa otro numero: '))

if num_2 == 0:
	print('no se puedee dividir entre 0')
else:
	divi = num_1 / num_2
	print('la division es:', divi)
	