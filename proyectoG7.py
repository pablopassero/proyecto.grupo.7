#Proyecto G 7 
#Alumnos:
#Alumnos:Juan Pablo Zarza,Fernando Tomás Burgos
import random

# Función para seleccionar una palabra aleatoria de la lista
def seleccionar_palabra():
    palabras = ["python", "programacion", "informatorio", "boca", "septima", "ahorcado"]
    return random.choice(palabras)

# Función para inicializar el juego y establecer las variables iniciales
def inicializar_juego():
    palabra_secreta = seleccionar_palabra()
    intentos_restantes = 6
    letras_adivinadas = []
    letras_incorrectas = []
    return palabra_secreta, intentos_restantes, letras_adivinadas, letras_incorrectas

# Función para mostrar el estado actual del juego
def mostrar_estado(palabra_secreta, letras_adivinadas, letras_incorrectas, intentos_restantes):
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    print("Palabra: " + palabra_mostrada)
    print("Letras incorrectas: " + ", ".join(letras_incorrectas))
    print("Intentos restantes: " + str(intentos_restantes))

    while intentos > 0:
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto! Letras adivinadas:", " ".join(letras_adivinadas))
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")

        palabra_oculta = mostrar_palabra(palabra_secreta, letras_adivinadas)
        print(palabra_oculta)

        if palabra_oculta == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break

    if intentos == 0:
        print("Has perdido. La palabra era:", palabra_secreta)
