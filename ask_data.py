import json

with open("output.json", "r", encoding="utf-8") as file:
    personas = json.load(file)

while True:
    cuit = input("Introduzca el CUIT de la persona: ")

    persona = personas.get(cuit)

    if persona:
        print(f"Datos de la persona con CUIT {cuit}:")
        print(f"Denominación: {persona['denominacion']}")
        print(f"Impuesto Ganancias: {persona['imp_ganancias']}")
        print(f"Impuesto IVA: {persona['imp_iva']}")
        print(f"Monotributo: {persona['monotributo']}")
        print(f"Integrante Soc: {persona['integrante_soc']}")
        print(f"Empleador: {persona['empleador']}")
        print(f"Actividad Monotributo: {persona['actividad_monotributo']}")
    else:
        print(f"No se encontró a la persona con CUIT {cuit}")
