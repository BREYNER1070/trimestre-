aggMaterias = []
cantidad = int(input("cuantas materias quieres agregar: "))
for i in range(cantidad):
    materias =input(f"ingrese la materia {i+1}:")
    aggMaterias.append(materias)
print("\n Las materias que agregaste son:")
for n in aggMaterias:
    print("°",n)