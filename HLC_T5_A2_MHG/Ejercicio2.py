num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

print ("Los números ingresador por el usuario son: ", num1,', ',num2,', ',num3)

if num1 > num2 and num1 > num3:
    print(f"El mayor número es: {num1}")
    
elif num2 > num1 and num2 > num3:
    print(f"El mayor número es: {num2}")
    
elif num3 > num1 and num3 > num2:
    print(f"El mayor número es: {num3}")
    
else:
    print("Los tres numeros son iguales")