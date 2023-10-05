import datetime

año_actual = datetime.datetime.now().year

año_nacimiento = int(input("Ingrese su año de nacimiento: "))

edad = año_actual - año_nacimiento

print(f"Su edad es aproximadamente de: {edad} años, ¿ya esta cuchito?")

"""Programa que permita calcular la edad de una persona 
conociendo el año actual y el usuario digita su año de nacimiento."""