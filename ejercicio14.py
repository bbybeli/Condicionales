# Diccionario que mapea los meses a su número de días
dias_mes = {
    1: 31,  # Enero
    2: 28,  # Febrero (no considera años bisiestos)
    3: 31,  # Marzo
    4: 30,  # Abril
    5: 31,  # Mayo
    6: 30,  # Junio
    7: 31,  # Julio
    8: 31,  # Agosto
    9: 30,  # Septiembre
    10: 31, # Octubre
    11: 30, # Noviembre
    12: 31  # Diciembre
}

# Leer el número del mes
mes = int(input("Introduce un número de mes (1-12): "))

# Verificar si el mes está en el rango
if mes in dias_mes:
    print(f"El mes {mes} tiene {dias_mes[mes]} días.")
else:
    print("ERROR: número incorrecto.")
