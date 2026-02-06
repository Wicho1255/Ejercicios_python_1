#Definir x1,y1,x2,y2,r1,r2 Como Real; 
import math
#Definir distancia Como Real;
print("Dime coordenada x primera circunferencia:")
x1 = float(input())
print("Dime coordenada y primera circunferencia:")
y1 = float(input())
print("Dime radio primera circunferencia:")
r1 = float(input())
print("Dime coordenada x segunda circunferencia:")
x2 = float(input())
print("Dime coordenada y segunda circunferencia:")
y2 = float(input())
print("Dime radio segunda circunferencia:")
r2 = float(input())

distancia = math.sqrt((x2  - x1) ** 2 + (y2 - y1) ** 2);
#circunferencias exteriores
#La distancia entre los centros, d, es mayor que la suma de los radios.
if distancia > (r1 + r2) :
	print("Circunferencias exteriores")

#circunferencias tangentes exteriores
#La distancia entre los centros es igual a la suma de los radios.
if distancia == (r1 + r2) :
	print("Circunferencias tangentes exteriores")

#circunferencias secantes
#La distancia  es menor que la suma de los radios y mayor que su diferencia.
if distancia < (r1 + r2) and distancia > abs(r1 - r2) :
	print("Circunferencias secantes")

#Circunferencias tangentes interiores
#La distancia entre los centros es igual a la diferencia entre los radios.
if distancia == abs(r1 - r2) :
	print("Circunferencias tangentes interiores")
#Circunferencias interiores
#La distancia entre los centros es mayor que cero y menor que la diferencia entre los radios. 
if distancia> 0 and distancia < abs(r1-r2) :
	print("Circunferencias interiores")
#Circunferencias concétricas
#La distancia = 0.
if distancia == 0 :
	print("Circunferencias concétricas")