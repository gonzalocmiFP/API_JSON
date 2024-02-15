import json

with open('employees.json') as archivo:
    data = json.load(archivo)

empleados_no_gronk = []

for empleado in data:
    salario = float(empleado["salary"].replace("$", "").replace(",", ""))

    if empleado["age"] < 30:
        salarioAumentado = salario * 1.1
        empleado["salary"] = f"€{salarioAumentado:,}"
    else:
        empleado["salary"] = f"€{salario:,}"

    if empleado["proyect"] != "GRONK":
        empleados_no_gronk.append(empleado)

for empleado in empleados_no_gronk:
    empleado["salary"] = empleado["salary"].replace("$", "€")
    print(empleado)