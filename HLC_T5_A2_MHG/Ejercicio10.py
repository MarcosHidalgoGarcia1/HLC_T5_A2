def dibuja():
    num_estrellas = int(input("Introduce el número de estrellas: "))
    
    estrella="★ "
    for index in range (1, num_estrellas+1):
            print (estrella*index)
dibuja()
