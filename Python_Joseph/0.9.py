#Programa que permita a una tienda saber el valor que pagara un cliente por la 
# compra de varios elementos de la misma referencia. Debe tener como entradas el valor 
# unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

valor_unitario = float(input("Digite el valor unitario del producto: "))

cantidad = int(input("Digite la cantidad de productos que desea llevar del ARA: "))

costo_sin_iva = valor_unitario * cantidad

iva = 0.16 * costo_sin_iva

costo_total = costo_sin_iva + iva

print(f"El valor total de {cantidad} productos a {valor_unitario} cada uno es de ${costo_total:.2f} (incluyendo el 16% del iva)")
