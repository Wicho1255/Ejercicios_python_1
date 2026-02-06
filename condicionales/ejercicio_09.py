#Análisis
#Debemos preguntar cuanto dinero es la compra, calcular el 15% y restarlo al total.
#Datos de entrada: precio (real).
#Información de salida: precio final (real).
#Variables: precio(real).
#Diseño
#1. Leer el precio
#2. Mostrar precio final: precio - 15% del precio

#Proceso CalcularPrecio
#Definir precio como Real

print("Dime el precio:")
precio = float(input())
print ("Precio final:", precio - precio * 0.15)