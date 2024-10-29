# Leer una cadena desde el teclado
cadena = input("Introduce una cadena: ")

# la cadena es una letra mayúscula
if len(cadena) == 1 and cadena.isupper():
    print(f"{cadena} es una letra mayúscula.")
else:
    print(f"{cadena} no es una letra mayúscula.")
