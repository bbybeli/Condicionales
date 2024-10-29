# Función para calcular el costo de la llamada
def calcular_costo_llamada(duracion, dia, turno):
    # Costo base de la llamada
    if duracion <= 5:
        costo = 1.0
    elif duracion <= 8:
        costo = 1.0 + (duracion - 5) * 0.80
    elif duracion <= 10:
        costo = 1.0 + (3 * 0.80) + (duracion - 8) * 0.70
    else:
        costo = 1.0 + (3 * 0.80) + (2 * 0.70) + (duracion - 10) * 0.50

    # Cálculo del impuesto según el día y turno
    if dia.lower() == "domingo":
        impuesto = 0.03  # 3%
    elif turno.lower() == "mañana":
        impuesto = 0.15  # 15%
    elif turno.lower() == "tarde":
        impuesto = 0.10  # 10%
    else:
        impuesto = 0.0  # Sin impuesto

    # Calcular el total con el impuesto
    total = costo * (1 + impuesto)
    return costo, impuesto * costo, total

# Leer la duración de la llamada, el día y el turno
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana: ")
turno = input("Introduce el turno (mañana/tarde): ")

# Calcular los costos
costo_base, impuesto, total = calcular_costo_llamada(duracion, dia, turno)

# Mostrar los resultados
print(f"Costo base de la llamada: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {impuesto:.2f} euros")
print(f"Costo total a pagar: {total:.2f} euros")
