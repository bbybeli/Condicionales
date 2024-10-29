# Leer la nota, la edad y el sexo desde el teclado
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ").upper()

# Verificar las condiciones y mostrar el mensaje correspondiente
if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")
