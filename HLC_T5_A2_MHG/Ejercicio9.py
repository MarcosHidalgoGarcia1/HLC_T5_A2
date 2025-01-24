

def adivinar_numero():
    import random
    numero_secreto = random.randint(1, 50)
    adivinar = False
    print("Adivina el número entre el 1 y el 50")

    while not adivinar:
        intento = int(input("introduce el número: "))

        if intento < numero_secreto:
            print("Más alto")
            
        elif intento > numero_secreto:
            print("Más bajo")
            
        else:
            print("¡Felicidades! Has adivinado el número ", numero_secreto)
            
            adivinar = True
adivinar_numero()
