def check_pass():
    contraseña = "secreta123"
    tries = 0
    
    while tries < 3:
        user_pass = input ("Introduce tu contraseña: ")
        if contraseña == user_pass:
            print("Bienvenido")
            break
        else:
            tries += 1
            
check_pass()