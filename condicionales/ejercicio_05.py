#programa que valide usuario y contraseña

user = 'admin'
password = 'qwerty'

usuario = input('ingresa tu usuario: ')
contraseña = input('ingresa tu contraseña:')

if user == usuario and password == contraseña:
	print('has entrada al sistema')
else:
	print('error de acceso')