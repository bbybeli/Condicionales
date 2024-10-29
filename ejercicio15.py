# Determinar el resultado del juego
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "papel" and opcion2 == "piedra") or \
         (opcion1 == "tijera" and opcion2 == "papel"):
        return "Gana jugador 1"
    else:
        return "Gana jugador 2"

# Leer las opciones de los jugadores
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Opciones válidas
opciones_validas = {"piedra", "papel", "tijera"}

# Verificar si las opciones son válidas
if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Opción incorrecta. Asegúrate de elegir entre piedra, papel o tijera.")
else:
    #El resultado
    resultado = determinar_ganador(jugador1, jugador2)
    print(resultado)
