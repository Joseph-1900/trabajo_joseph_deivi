"""Programa que solicite un número al usuario y permita calcular la raíz 
cuadrada del mismo (sin usar función). """


numero = float(input("Por favor, introduce un número para calcular su raíz cuadrada: "))

raiz_aproximada = numero / 2

max_iteraciones = 100

for _ in range(max_iteraciones):
    raiz_aproximada = 0.5 * (raiz_aproximada + numero / raiz_aproximada)
print(f"La raíz cuadrada de {numero} es aproximadamente {raiz_aproximada:.6f}")
print("GRACIAS :D")
