import random
import string

def generar_contraseña(tamano):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(tamano))
    return contraseña

# Entrada del usuario
user_dificultad = int(input("¿De cuántos dígitos queres tu contraseña?: "))
for _ in range(4): # Generar 5 contraseñas
    print("Tus contraseñas generadas son:", generar_contraseña(user_dificultad))