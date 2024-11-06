import requests
from datetime import datetime as dt
import time


def get_cotizacion():
    response = requests.get("https://criptoya.com/api/dolar")
    response.raise_for_status()
    data_mep = response.json()
    price_mep = data_mep['mep']['al30']['ci']['price']
    # Return both compra and venta as a tuple
    return price_mep, price_mep


if __name__ == "__main__":
    last_venta_mep_dmep = None

    while True:
        try:
            # Obtener datos de la API
            response = requests.get("https://criptoya.com/api/dolar")
            response.raise_for_status()
            
            data_mep = response.json()
            venta_mep_dmep = data_mep['mep']['al30']['ci']['price']
            fecha_mep_dmep = dt.now()
            
            last_venta_mep_dmep = venta_mep_dmep
            
            print(f"VENTA Coti mep: {venta_mep_dmep:.2f}")
        except Exception as e:
            print(f"Me rompi: {str(e)}")

        time.sleep(6)

