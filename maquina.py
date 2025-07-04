total = 0 
print("Maquina expendedora")

print("1, Cafe 3000")
print("2, te 2500")
print("3, jugo 3500")
print("0, salir ")

while True:
    escoger = int(input("escoge una opcion (1,2,3 o 0 salir): "))
    match escoger:
        case 1:
                print("seleccionaste el cafe se le sumara 3000 a tu pago: ")
                total += 3000
        case 2: 
                print("seleccionaste el te se le sumara 2500 a tu pago: ")
                total += 2500
        case 3:
                print("seleccionaste el jugo se le sumara 3500 a tu pago: ")
                total += 3500
        case 0:
            if escoger == 0:
                print("Haz salido del programa")
                break 
        case _:
                print("opcion incorrecta ")
print(f"tu pago total va a ser {total}")