Este simple script permite procesar la base de datos de contribuyentes de impuestos nacionales registrados en AFIP, para poder realizar facilmente consultas según la denominación del contribuyente o el número de CUIT.
Se puede descargar la base de datos pública, difundida por el organismo oficial desde su sitio web: [AFIP constancia de inscripción a impuestos](https://www.afip.gob.ar/genericos/cInscripcion/archivoCompleto.asp)

## Funcionamiento

### Ejecución de process_data.py
![image](https://github.com/user-attachments/assets/8ff88475-ed06-4af3-80b2-4d81bd6b8dc2)
![image](https://github.com/user-attachments/assets/ac8e71f1-04b5-4417-89ee-d3d94b860424)

### Ejecución de get_data.py

![image](https://github.com/user-attachments/assets/9629ad01-1312-4d00-975a-90fd333ce969)

![image](https://github.com/user-attachments/assets/b83ba589-955c-4a3c-88e6-603f07a6a3a4)


## AFIP file

![image](https://github.com/user-attachments/assets/6f4e5cfe-c721-4080-9ecf-a5d018f1ba7b)


## Output file

![image](https://github.com/user-attachments/assets/c0256713-a430-4642-be1f-6f175d75471e)


## Size

![image](https://github.com/user-attachments/assets/5ca500ef-43ff-49c6-be46-cdd75b37ff6b)

## Referencias
![image](https://github.com/user-attachments/assets/7a381ca3-afa3-44a4-86d6-bdfca5a048bf)

## Uso
1. Descargar el repositorio
```bash
git clone https://github.com/TobiasCoding/get-data-by-argentinian-CUIT.git
```
2. Ir al directorio del repositorio
```
cd get-data-by-argentinian-CUIT
```
2. Descargar archivo en formato ZIP de https://www.afip.gob.ar/genericos/cInscripcion/archivoCompleto.asp y guardar en el mismo directorio del repositorio descargado
3. Descomprimir el archivo descargado
```bash
unzip apellidoNombreDenominacion.zip
```
4. Generar el archivo de base de datos (una única vez)
```bash
python3 process_data.py
```
5. Ejecutar el script (las veces que deseemos)
```bash
python3 ask_data.py
```
---

Desarrollado por Tobias Rímoli.
Contacto: tobiasrimoli@duck.com
