barras = int(input("Introduce el núumero de barras vendidas que no son frescas: "))
precio = 3.50
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "$")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " +str(round(coste, 2)) +"$")
      
