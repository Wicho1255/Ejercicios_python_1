#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
#cuantas horas y minutos corresponde.

minutos = int(input('Dime una cantidad de minutos; '))
horas = (minutos // 60);
minutos = minutos % 60;

print(horas," horas y ",minutos ," minutos.")