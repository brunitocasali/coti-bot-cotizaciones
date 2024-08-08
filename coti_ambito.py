import requests
import time
from database import cursor

def get_cotizacion():
    response = requests.get("https://mercados.ambito.com/dolar/informal/variacion")
    response.raise_for_status()  # Handle HTTP errors
    
    # Parse the JSON response
    data_usd = response.json()

    return (
        float(data_usd['compra'].replace(',', '.')),
        float(data_usd['venta'].replace(',', '.'))
    )


if __name__ == '__main__':
    while True:
        try:
            response = requests.get("https://mercados.ambito.com/dolar/informal/variacion")
            response.raise_for_status()  # Handle HTTP errors
            
            # Parse the JSON response
            data_usd = response.json()

            #valores ambito
            compra_usd_amb = data_usd['compra']
            venta_usd_amb = data_usd['venta']
            fecha_usd_amb = data_usd['fecha']
            variacion_usd_amb = data_usd['variacion']

            print(compra_usd_amb)
            print(venta_usd_amb)
            print(fecha_usd_amb)
            print(variacion_usd_amb)

            print('////////////////')

        
            
            coti_compra = float(data_usd['compra'].replace(',', '.')) * 0.995
            coti_venta = float(data_usd['venta'].replace(',', '.')) +5
            print(f"Compra Coti USD: {coti_compra:.2f}")
            print(data_usd) 
            
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            # Optional: wait before retrying in case of an error
        time.sleep(6)

