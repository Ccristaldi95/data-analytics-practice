import random
numero_secreto=random.randint(1,100)
adivinado=False
cantidad_intentos=0
cant_max_intentos=5

print("Bienvenido al juego de adivinar el número secreto")
while not adivinado and cantidad_intentos < cant_max_intentos:
     entrada= input("Introduce un número del 1 al 99: ")
     numero=int(entrada)

     if numero==numero_secreto:
        print("Felicidades has adivinado el número secreto")
        adivinado= True

     elif numero < numero_secreto:
        print("El número es mayor al ingresado")

     else: 
        print("El número es menor al ingresado")
        
     cantidad_intentos += 1

if  not cantidad_intentos < cant_max_intentos:
    print("Game over! No has podido adivinar el número secreto")
