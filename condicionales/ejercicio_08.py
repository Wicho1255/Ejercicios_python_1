#Proceso CalcularSueldo
#Definir sueldo_base, venta1, venta2, venta3, comision como Real;
print("Dime el sueldo base:")
sueldo_base = int(input())
print("Dime precio de la venta 1:")
venta1 = int(input())
print("Dime precio de la venta 2:")
venta2 = int(input())
print("Dime precio de la venta 3:")
venta3 = int(input())
comision = venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1
print("Comisión por ventas:",comision)
print("Sueldo total:", sueldo_base + comision)