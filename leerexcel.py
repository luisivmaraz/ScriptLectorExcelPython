import pandas as pd
import requests
import time
import hashlib

def hash_file(file_path):
    """Calcula el hash SHA-256 del archivo."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def send_new_rows(df_previous, df_current, api_url):
    """Envía nuevas filas de df_current que no están en df_previous a la API."""
    new_rows = df_current[~df_current.index.isin(df_previous.index)]
    print("Nuevas filas identificadas:", new_rows)
    if not new_rows.empty:
        for index, row in new_rows.iterrows():
            json_base = {
                "status": "Valid", 
                "typeSensor": "maxbotix",
                "sensorData": 00, 
                "unit": "cm", 
                "parameter": "NA"
            }
            json_data = json_base.copy()
            json_data['sensorData'] = row['Dato1']
            json_data['status'] = row['Dato2']

            response = requests.post(api_url, json=json_data)
            if response.status_code == 200:
                print(f'Fila {index} enviada correctamente.')
            else:
                print(f'Error al enviar la fila {index}: {response.status_code}, {response.text}')

if __name__ == "__main__":
    archivo_excel = 'C:/Users/luisi/OneDrive/Escritorio/testdepy.xlsx'
    hoja = 'Hoja1'
    api_url = 'http://localhost:3200/'

    df_previous = pd.read_excel(archivo_excel, sheet_name=hoja)
    last_hash = hash_file(archivo_excel)
    print("Observando cambios en el archivo Excel...")

    try:
        while True:
            time.sleep(5)  # temporizador para volver a enalizar el excel para encontrar cambis 
            current_hash = hash_file(archivo_excel)
            if current_hash != last_hash:
                print("El archivo ha cambiado. Procesando...")
                df_current = pd.read_excel(archivo_excel, sheet_name=hoja)
                send_new_rows(df_previous, df_current, api_url)
                df_previous = df_current
                last_hash = current_hash
            else:
                print("No hay cambios en el archivo.")
    except KeyboardInterrupt:
        print("Proceso terminado manualmente.")
