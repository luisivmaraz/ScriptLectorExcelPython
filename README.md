# Monitoreo y Envío de Cambios desde Excel a una API

Este proyecto es un script en Python que supervisa un archivo Excel para detectar cambios y envía nuevas filas a una API. Es útil para aplicaciones donde se necesita integrar datos dinámicos desde un archivo Excel con sistemas externos.

---

## Características

- **Detección de Cambios:** Supervisa un archivo Excel y detecta modificaciones en tiempo real.
- **Cálculo de Hash SHA-256:** Utiliza el hash del archivo para identificar cambios.
- **Identificación de Nuevas Filas:** Compara el archivo actualizado con el anterior y extrae las nuevas filas.
- **Envío a una API:** Envía las nuevas filas como solicitudes POST en formato JSON a una API específica.

---

## Requisitos Previos

1. **Python 3.8 o superior.**
2. **Librerías necesarias:**  
   Instalar las siguientes librerías usando pip:
   ```bash
   pip install pandas requests openpyxl
   ```
3. **Un archivo Excel** con la estructura esperada:
   - `Dato1`: Datos numéricos (sensorData).
   - `Dato2`: Estado del sensor (status).

4. **Una API receptora:** Debe aceptar solicitudes POST en el endpoint especificado (`http://localhost:3200/` por defecto).

---

## Uso

1. **Configuración del Archivo Excel:**
   - Modificar el archivo `testdepy.xlsx` en la ruta:  
     `C:/Users/luisi/OneDrive/Escritorio/testdepy.xlsx`.
   - Asegúrate de que contiene una hoja llamada `Hoja1`.

2. **Configurar el Endpoint de la API:**
   - Actualizar la variable `api_url` con la URL de la API.

3. **Ejecutar el Script:**
   - Ejecuta el script en tu terminal:
     ```bash
     python script.py
     ```
   - El programa supervisará continuamente el archivo y enviará nuevas filas a la API.

4. **Detener la Ejecución:**
   - Presiona `Ctrl + C` para detener el programa.

---

## Funciones Principales

### `hash_file(file_path)`
Calcula el hash SHA-256 de un archivo para detectar cambios.

### `send_new_rows(df_previous, df_current, api_url)`
Identifica nuevas filas en el archivo actualizado y las envía como solicitudes POST a la API.

### `main`
Supervisa el archivo Excel en tiempo real y procesa cambios automáticamente.

---

## Ejemplo de JSON Enviado

Cada fila nueva se convierte en un JSON como el siguiente:
```json
{
  "status": "Valid",
  "typeSensor": "maxbotix",
  "sensorData": 12.5,
  "unit": "cm",
  "parameter": "NA"
}
```

---

## Consideraciones

1. **Rendimiento:** Configura el intervalo de supervisión (`time.sleep`) según las necesidades.
2. **Errores de Red:** Maneja los errores de conexión a la API y añade reintentos si es necesario.
3. **Formato de Excel:** Asegúrate de que los datos en el Excel coincidan con los campos esperados.

