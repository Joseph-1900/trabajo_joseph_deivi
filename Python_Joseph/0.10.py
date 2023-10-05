"""Programa que permita determinar el salario a pagar a un empleado, 
teniendo como entradas el salario diario y el número de días trabajados. 
Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% 
por concepto de salud."""

salario_diario = float(input("Digite por favor el salario diario del empleado: "))

dias_trabajados = int(input("Digite por favor el numero de dias trabajados: "))

salario = salario_diario * dias_trabajados

descuento_de_pension = 0.10 * salario

descuento_de_salud = 0.15 * salario

salario_neto = salario - descuento_de_pension - descuento_de_salud
print(f"El salario que se le debe pagas al empleado es de: {salario_neto:.2f}")