import requests
from datetime import datetime as dt
import time


def get_cotizacion():
    response = requests.get("https://criptoya.com/api/dolar")
    response.raise_for_status()  # Para manejar errores HTTP

    data_usd_ccl = response.json()

    # Cotizaciones actuales del dólar ccl
    return data_usd_ccl['ccl']['ask'], data_usd_ccl['ccl']['bid']


# Función para calcular la variación porcentual
def calcular_variacion(actual, anterior):
    if anterior is None:
        return None  # No hay valor anterior para comparar
    return ((actual - anterior) / anterior) * 100


if __name__ == "__main__":
    # Variables para almacenar las últimas cotizaciones
    last_compra_usd_ccl_cy = None
    last_venta_usd_ccl_cy = None

    # Bucle para actualizar y calcular cotizaciones
    while True:
        try:
            # Obtener datos de la API
            response = requests.get("https://criptoya.com/api/dolar")
            response.raise_for_status()  # Para manejar errores HTTP

            data_usdt = response.json()

            # Cotizaciones actuales del dólar ccl
            compra_usd_ccl_cy = data_usdt['ccl']['ask']
            venta_usd_ccl_cy = data_usdt['ccl']['bid']
            fecha_usd_ccl_cy = dt.now()

            # Calcular variaciones
            variacion_compra = calcular_variacion(compra_usd_ccl_cy, last_compra_usd_ccl_cy)
            variacion_venta = calcular_variacion(venta_usd_ccl_cy, last_venta_usd_ccl_cy)
            variacion_usdt_fw = (variacion_compra + variacion_venta) / 2 if variacion_compra is not None and variacion_venta is not None else None

            # Mostrar resultados
            print(f"COMPRA USD: {compra_usd_ccl_cy:.2f}")
            print(f"VENTA USD: {venta_usd_ccl_cy:.2f}")
            print(f"Fecha: {fecha_usd_ccl_cy}")

            if variacion_compra is not None:
                print(f"Variación COMPRA: {variacion_compra:.2f}%")
            else:
                print("No hay variación anterior para COMPRA.")

            if variacion_venta is not None:
                print(f"Variación VENTA: {variacion_venta:.2f}%")
            else:
                print("No hay variación anterior para VENTA.")

            

            
           

            
        except:
            print("Me rompi")

        # Esperar 60 segundos antes de la próxima actualización
        time.sleep(60)
