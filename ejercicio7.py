# Leer la base y el exponente desde el teclado
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calcular la potencia según el valor del exponente
if exponente > 0:
    resultado = base ** exponente
    print(f"{base} elevado a {exponente} es {resultado}.")
elif exponente == 0:
    print(f"{base} elevado a {exponente} es 1.")
else:  # exponente negativo
    resultado = 1 / (base ** abs(exponente))
    print(f"{base} elevado a {exponente} es {resultado}.")
