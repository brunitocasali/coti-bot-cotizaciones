import requests
import time
import gspread
from google.oauth2.service_account import Credentials

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account_key.json'

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Authenticate and create the service client
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)

# Open the Google Sheets file and select the sheet
spreadsheet = client.open('your_spreadsheet_name')
sheet = spreadsheet.sheet1  # Use the sheet name or index

def fetch_data():
    response = requests.get("https://dolarapi.com/v1/ambito/dolares/blue")
    data = response.json()
    compra = data.get("compra")
    venta = data.get("venta")
    fecha = data.get("fechaActualizacion")
    
    # Convertir ambito a float
    compra_amb = float(compra)
    venta_amb = float(venta)
    
    # Calcular Coti
    compra_coti = compra_amb - 5
    venta_coti = venta_amb + 5

    # Def cotizacion ambito as list
    cotizacion_amb = [compra, venta, fecha]

    # Def Cotizacion Coti
    cotizacion_coti = [compra_coti, venta_coti, fecha]

    return cotizacion_amb, cotizacion_coti

while True:
    # Hacer una solicitud a la API
    response = requests.get("https://dolarapi.com/v1/ambito/dolares/blue")
    
    # Analizar la respuesta JSON
    data = response.json()
    
    # Acceder a los diferentes valores del JSON
    compra = data.get("compra")
    venta = data.get("venta")
    fecha = data.get("fechaActualizacion")
    
    #Convertir ambito a float
    compra_amb = float(compra)
    venta_amb = float(venta)
    
    #Calcular Coti
    compra_coti = compra_amb - 5
    venta_coti = venta_amb + 5

    #Def cotizacion ambito as list
    cotizacion_amb = [compra, venta, fecha]
    #Venta Euro pesos
    v_eur_coti = venta_amb * 1.1575
    c_eur_coti  = compra_amb * 1.14

    #Def Cotizacion Coti
    cotizacion_coti = [compra_coti, venta_coti, c_eur_coti, v_eur_coti, fecha]

    # Imprimir los valores Ambito
    print("Cotizaciones Ambito:")
    print(cotizacion_amb[0])
    print(cotizacion_amb[1])
    print(cotizacion_amb[2])
    print("/////////////////////")
    
    #Imprimir valores Coti
    print("Coti:")
    print("Compra USD: ", cotizacion_coti[0])
    print("Venta USD: ",cotizacion_coti[1])
    print("Compra EUR: ",cotizacion_coti[2])
    print("Venta EUR: ",cotizacion_coti[3])
    print("Fecha:" , cotizacion_coti[4])
    print('//////////////')


        # Esperar 60 segundos antes de la siguiente solicitud
    time.sleep(5)