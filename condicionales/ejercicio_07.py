#Proceso CalcularHoras
#Definir minutos, res_horas, res_min como Entero;
print("Dime la cantidad de minutos:")
minutos = int(input())
res_horas = (minutos // 60)
res_min = minutos % 60
print(res_horas," horas y ",res_min," minutos.")