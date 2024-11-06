import requests
from datetime import datetime as dt
import time


def get_cotizacion():
    response = requests.get("https://criptoya.com/api/dolar")
    response.raise_for_status()
    data_ccl = response.json()
    price = data_ccl['ccl']['al30']['ci']['price']
    # Store the same price for both compra and venta since there's no spread
    return price, price  # This will store price in both COMPRA and VENTA columns


if __name__ == "__main__":
    last_venta_ccl = None

    while True:
        try:
            # Obtener datos de la API
            response = requests.get("https://criptoya.com/api/dolar")
            response.raise_for_status()
            
            data_ccl = response.json()
            venta_ccl = data_ccl['ccl']['al30']['ci']['price']
            fecha_ccl = dt.now()
            
            last_venta_ccl = venta_ccl
            
            print(f"VENTA Coti CCL: {venta_ccl:.2f}")
        except Exception as e:
            print(f"Me rompi: {str(e)}")

        time.sleep(6)

