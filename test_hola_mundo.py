# Simula una "prueba" verificando que el saludo sea correcto

# def prueba():
#     mensaje = "Hola Mundo desde Python"
#     if "Hola" in mensaje:
#         print("Este es un hola desde Python en Jenkins")
#         exit(0)
#     else:
#         print("Prueba fallida: ha ocurrido un error")
#         exit(1)

# prueba()




from holaMundo import obtener_saludo

def test_hola_mundo():
    nombre = "Carolina"
    saludo = obtener_saludo(nombre)
    
    if saludo == f"Hola {nombre}, bienvenido a Jenkins!":
        print("✅ Prueba exitosa: El saludo es correcto.")
    else:
        print("❌ Prueba fallida: El saludo no es el esperado.")
        exit(1)  # Esto hace que Jenkins detecte el fallo
