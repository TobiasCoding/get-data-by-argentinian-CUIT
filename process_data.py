import glob, os, json

directory = os.path.join("utlfile", "padr")
input_files = glob.glob(os.path.join(directory, "*"))

if input_files:
    input_file = input_files[0]
    print("Archivo encontrado: {input_file}")
else:
    print(f"No se encontraron archivos en el directorio '{directory}'.")
    exit()

output_file = "argentinians_data.json"

data = {}

with open(input_file, "r", encoding="latin-1") as file:
    lines = sum(1 for line in file)
    print(f"El archivo tiene {str(lines)} registros")

    file.seek(0)  # Reiniciar el puntero del archivo al inicio

    i = 0
    for line in file:
        # Extracción de cada campo basado en la posición (segun referencias de AFIP: https://www.afip.gob.ar/genericos/cInscripcion/archivoCompleto.asp
        cuit = line[0:11].strip()
        denominacion = line[11:41].strip()
        imp_ganancias = line[41:43].strip()
        imp_iva = line[43:45].strip()
        monotributo = line[45:47].strip()
        integrante_soc = line[47:48].strip()
        empleador = line[48:49].strip()
        actividad_monotributo = line[50:52].strip()

        # Creación de la estructura de datos anidada
        data[cuit] = {
            "denominacion": denominacion,
            "imp_ganancias": imp_ganancias,
            "imp_iva": imp_iva,
            "monotributo": monotributo,
            "integrante_soc": integrante_soc,
            "empleador": empleador,
            "actividad_monotributo": actividad_monotributo
        }
        i+=1
        print(f'''Progreso: {i / lines * 100:.1f}% completado''', end='\r')

print("Guardando archivo")
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"El archivo {output_file} ha sido creado con éxito.")
