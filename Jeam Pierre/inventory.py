articulos = []

cantidad = int(input("¿Cuántos productos deseas agregar? "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    stock = int(input(f"Ingrese la cantidad disponible de {nombre}: "))
    articulos.append([nombre, stock])

print("\nProductos disponibles en inventario:")
for producto in articulos:
    if producto[1] > 0:
        print(producto[0], "-", producto[1], "unidades")