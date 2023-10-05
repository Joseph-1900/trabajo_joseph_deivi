valor=int(input("Coloca el valor del pago: "))
cant=int(input("Coloca los dias trabajados: "))

pago= valor* cant
multi= pago * 0.10
descuento= pago- multi
salud= descuento * 0.15
total =descuento - salud

print(f"Finalizado gracias y pago total es de:{pago} el descuento del 10% es de:{descuento} y se le descuenta el 15% a la salud es de:{total}") 
