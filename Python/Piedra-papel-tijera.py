
Jugador1= input("Hola Jugador 1! Que eliges? Piedra, papel o tijera?: ").lower().strip()
Jugador2=input("Hola Jugador 2! Que eliges? Piedra, papel o tijera?: ").lower().strip()


condicion1= Jugador1 == "piedra" and Jugador2 == "tijera"
condicion2= Jugador1 == "papel" and Jugador2 == "piedra"
condicion3= Jugador1 == "tijera" and Jugador2== "papel"

if Jugador1 == Jugador2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado: Jugador 1")
else:
    print("Ha ganado el jugador 2!")
