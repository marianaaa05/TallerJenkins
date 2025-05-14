# Simula una "prueba" verificando que el saludo sea correcto

def prueba():
    mensaje = "Hola Mundo desde Python"
    if "Hola" in mensaje:
        print("Prueba pasada: 'Hola' está en el mensaje.")
        exit(0)
    else:
        print("Prueba fallida: 'Hola' no está en el mensaje.")
        exit(1)

prueba()
