import random
ganadas = 0 
perdidas = 0
print("JUEGO DE JUGADOR Y BANCA")
print("si")
print("no")  

while ganadas < 5 and  perdidas < 3:
    escoger = str(input("QUIERES JUGAR  (si / no): "))
    match escoger:
        case 1 :
            if escoger == "no":
                print("has dejado de jugar")
                break
        case 2:
            if escoger == "si":
             cartaUser = random.randint(1,13)
             cartaBanca = random.randint(1,13)
             print(f"tu carta es {cartaUser}")
             print(f"la carta de la banca es {cartaBanca}")
        case 3:
            if cartaBanca > cartaUser:
             print("perdiste")
             perdidas +=1
        case 4:
            if cartaUser > cartaBanca:
             print("ganaste")
            ganadas+=1
        case 5:
            if ganadas == 5:
                print("ganaste la partida")
        case 6:
            if perdidas == 3:
             print("perditste")
