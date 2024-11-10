Este simple script permite procesar la base de datos de contribuyentes de impuestos nacionales registrados en AFIP, para poder realizar facilmente consultas según el número de CUIT.
Se puede descargar la base de datos pública, difundida por el organismo oficial desde la página oficial: [AFIP constancia de inscripción a impuestos](https://www.afip.gob.ar/genericos/cInscripcion/archivoCompleto.asp)

## Funcionamiento

![image](https://github.com/user-attachments/assets/76a717a5-6f0a-41a8-8c0f-1bd658e02925)


## AFIP file

![image](https://github.com/user-attachments/assets/6f4e5cfe-c721-4080-9ecf-a5d018f1ba7b)


## Output file

![image](https://github.com/user-attachments/assets/c0256713-a430-4642-be1f-6f175d75471e)


## Size

![image](https://github.com/user-attachments/assets/1d5615e4-b54c-4b1b-a4da-9f61489cc0d1)


## Referencias
![image](https://github.com/user-attachments/assets/7a381ca3-afa3-44a4-86d6-bdfca5a048bf)

## Uso
1. 
```bash
git clone https://github.com/TobiasCoding/get-data-by-argentinian-CUIT.git
```
2. 
```
cd get-data-by-argentinian-CUIT
```
2. Descargar archivo en formato ZIP de https://www.afip.gob.ar/genericos/cInscripcion/archivoCompleto.asp y guardar en el mismo directorio del script
3. Descomprimir el archivo descargado
```bash
unzip apellidoNombreDenominacion.zip
```
3.
```bash
mv apellidoNombreDenominacion/utlfile/padr/*.tmp .
```
4. 
```bash
python3 process_data.py
```
5. 
```bash
python3 ask_data.py
```
