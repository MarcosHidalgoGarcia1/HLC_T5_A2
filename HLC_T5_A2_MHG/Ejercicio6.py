def check_chars():
    palabra = input("Introduce la palabra: ")
    
    for caracter in palabra:
        if "@" == caracter:
            print("La palabra tiene el caracter @")
        if "#" == caracter:
            print("La palabra tiene el caracter #")
        
check_chars()
        