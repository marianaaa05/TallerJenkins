# Simula una "prueba" verificando que el saludo sea correcto

def prueba():
    mensaje = "Hola Mundo desde Python"
    if "Hola" in mensaje:
        print("Este es un hola desde Python en Jenkins")
        exit(0)
    else:
        print("Prueba fallida: ha ocurrido un error")
        exit(1)

prueba()
