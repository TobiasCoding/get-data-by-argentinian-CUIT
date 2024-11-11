import json

with open("argentinians_data.json", "r", encoding="utf-8") as file:
    personas = json.load(file)

referencias = {
    "imp_ganancias": {
        "NI": "No Inscripto",
        "AC": "Activo",
        "EX": "Exento",
        "NC": "No corresponde",
    },
    "imp_iva": {
        "NI": "No Inscripto",
        "AC": "Activo",
        "EX": "Exento",
        "NA": "No alcanzado",
        "XN": "Exento no alcanzado",
        "AN": "Activo no alcanzado",
    },
    "monotributo": {
        "BT": "B trabajador promovido",
        "AP": "A actividad primaria",
        "AC": "A asociado a cooperativa",
        "AL": "A monotributo social locación",
        "AV": "A monotributo social ventas",
        "AT": "A trabajador promovido",
        "00": "No es monotributista",
        "01": "Comercial",
        "02": "Profesional",
        "03": "Servicios/Oficio",
        "04": "Industrial",
        "05": "Agropecuaria",
        "06": "Otros",
        "07": "Eventual",
        "08": "Prest. de Servicio o Locación",
        "09": "Otras actividades",
        "10": "Ventas",
        "11": "Agricultura Familiar",
    },
    "integrante_soc": {
        "N": "No activo",
        "S": "Activo",
    },
    "empleador": {
        "N": "No activo",
        "S": "Activo",
    },
    "actividad_monotributo": {
        "00": "No es monotributista",
        "01": "Comercial",
        "02": "Profesional",
        "03": "Servicios/Oficio",
        "04": "Industrial",
        "05": "Agropecuaria",
        "06": "Otros",
        "07": "Eventual",
        "08": "Prest. de Servicio o Locación",
        "09": "Otras actividades",
        "10": "Ventas",
        "11": "Agricultura Familiar",
    },
}

def mostrar_datos_persona(cuit, persona):
    print(f"\nDatos de la persona con CUIT {cuit}:")
    print(f"Denominación: {persona['denominacion']}")
    imp_ganancias = persona['imp_ganancias']
    print(f"Impuesto Ganancias: {imp_ganancias} ({referencias['imp_ganancias'].get(imp_ganancias, 'Desconocido')})")
    imp_iva = persona['imp_iva']
    print(f"Impuesto IVA: {imp_iva} ({referencias['imp_iva'].get(imp_iva, 'Desconocido')})")
    monotributo = persona['monotributo']
    print(f"Monotributo: {monotributo} ({referencias['monotributo'].get(monotributo, 'Desconocido')})")
    integrante_soc = persona['integrante_soc']
    print(f"Integrante Soc: {integrante_soc} ({referencias['integrante_soc'].get(integrante_soc, 'Desconocido')})")
    empleador = persona['empleador']
    print(f"Empleador: {empleador} ({referencias['empleador'].get(empleador, 'Desconocido')})")
    actividad_monotributo = persona['actividad_monotributo']
    print(f"Actividad Monotributo: {actividad_monotributo} ({referencias['actividad_monotributo'].get(actividad_monotributo, 'Desconocido')})")

print("Presione x para cerrar")

while True:
    opcion = input('''\n¿Desea buscar por CUIT o por denominación?
1. CUIT
2. Denominacion
3. Salir
> ''')
    if opcion == "3":
        break
    elif opcion == "1":
        cuit = input('''\nIntroduzca el CUIT de la persona o entidad:
> ''')
        if cuit == "3":
            break
        persona = personas.get(cuit)
        if persona:
            mostrar_datos_persona(cuit, persona)
        else:
            print(f"No se encontró a la persona con CUIT {cuit}")
    elif opcion == "2":
        denominacion_busqueda = input('''\nIntroduzca la denominación a buscar: 
> ''')
        if denominacion_busqueda == "3":
            break
        coincidencias = [cuit for cuit, persona in personas.items() if denominacion_busqueda.lower() in persona['denominacion'].lower()]
        
        if not coincidencias:
            print(f"No se encontraron personas con la denominación '{denominacion_busqueda}'.")
        elif len(coincidencias) == 1:
            cuit = coincidencias[0]
            mostrar_datos_persona(cuit, personas[cuit])
        else:
            print("\nSe encontraron múltiples coincidencias:")
            for index, cuit in enumerate(coincidencias, 1):
                print(f"{index}. CUIT: {cuit} - Denominación: {personas[cuit]['denominacion']}")
            
            seleccion = input("\nSeleccione el número de la persona para ver detalles o 'x' para cancelar: ")
            if seleccion.lower() == "x":
                continue
            try:
                seleccion_index = int(seleccion) - 1
                if 0 <= seleccion_index < len(coincidencias):
                    cuit = coincidencias[seleccion_index]
                    mostrar_datos_persona(cuit, personas[cuit])
                else:
                    print("Selección inválida.")
            except ValueError:
                print("Entrada inválida.")
    else:
        print("Opción no reconocida. Por favor ingrese el número de la opción (1, 2 o 3).")
