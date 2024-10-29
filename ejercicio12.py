# Función para obtener el número en letras
def numero_en_letras(num):
    letras = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis"
    }
    return letras.get(num, "ERROR: número incorrecto.")

# Leer el resultado del dado
resultado = int(input("Introduce el resultado del dado (1-6): "))

# Determinar la cara opuesta
if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    if resultado == 1:
        opuesto = 6
    elif resultado == 2:
        opuesto = 5
    elif resultado == 3:
        opuesto = 4
    elif resultado == 4:
        opuesto = 3
    elif resultado == 5:
        opuesto = 2
    elif resultado == 6:
        opuesto = 1

    # Obtener el número en letras
    opuesto_letras = numero_en_letras(opuesto)
    print(f"La cara opuesta a {resultado} es {opuesto_letras}.")
