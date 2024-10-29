# Leer el número de alumnos
num_alumnos = int(input("Introduce el número de alumnos: "))

# Inicializar variables
costo_por_alumno = 0
pago_compania = 0

# Determinar el costo según el número de alumnos
if num_alumnos >= 100:
    costo_por_alumno = 65
    pago_compania = costo_por_alumno * num_alumnos
elif num_alumnos >= 50:
    costo_por_alumno = 70
    pago_compania = costo_por_alumno * num_alumnos
elif num_alumnos >= 30:
    costo_por_alumno = 95
    pago_compania = costo_por_alumno * num_alumnos
else:
    costo_por_alumno = 4000  # Costo fijo si hay menos de 30 alumnos
    pago_compania = 4000

#  resultados
print(f"Costo por alumno: {costo_por_alumno} euros")
print(f"Pago total a la compañía de autobuses: {pago_compania} euros")
