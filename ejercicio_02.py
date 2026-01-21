#Calcular el perimetro y area de un rectangulo 
# Para realizar operaciones matematicas debemos

print("area y perimetro de un rectangulo")

base = input("Ingresa la base: ")
base = int(base)

altura = int(input("ingresa la altura: "))

area = base * altura
perimetro = base * 2 + altura * 2

print("area", area)
print ("perimetro", perimetro)