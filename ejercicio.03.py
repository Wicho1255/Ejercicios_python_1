#Dados los catetos de un triangulo rectangulo,
#calcular su hipotenusa

cateto_1 = int(input('Ingresa el cateto_1: '))
cateto_2 = int(input('Ingresa el cateto_2: '))

hipotenusa = (cateto_1 ** 2 + cateto_2 ** 2) ** (1/2)
print("la hipotenusa es: ", hipotenusa)