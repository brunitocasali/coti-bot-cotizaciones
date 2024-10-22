import requests
from datetime import datetime as dt
import time

def get_cotizacion():
    response = requests.get("https://criptoya.com/api/dolar")
    response.raise_for_status()  # Para manejar errores HTTP

    data_usd_ccl_cy = response.json()

    # Cotizaciones actuales del dólar CCL
    return data_usd_ccl_cy['ccl']['ci']['price']


# Función para calcular la variación porcentual
def calcular_variacion(actual, anterior):
    if anterior is None:
        return None  # No hay valor anterior para comparar
    return ((actual - anterior) / anterior) * 100


if __name__ == "__main__":
    # Variables para almacenar las últimas cotizaciones
    last_venta_usd_ccl_cy = None
    
    # Bucle para actualizar y calcular cotizaciones
    while True:
        try:
            # Obtener datos de la API
            response = requests.get("https://criptoya.com/api/dolar")
            response.raise_for_status()  # Para manejar errores HTTP

            data_usd_ccl_cy = response.json()

            # Cotizaciones actuales del dólar CCL
            venta_usd_ccl_cy = data_usd_ccl_cy['ccl']['ci']['price']
            fecha_usd_ccl_cy = dt.now()

            # Calcular variaciones
            variacion_venta = calcular_variacion(venta_usd_ccl_cy, last_venta_usd_ccl_cy)

            # Mostrar resultados
            print(f"VENTA USD: {venta_usd_ccl_cy:.2f}")
            print(f"Fecha: {fecha_usd_ccl_cy}")

            if variacion_venta is not None:
                print(f"Variación VENTA: {variacion_venta:.2f}%")
            else:
                print("No hay variación anterior para VENTA.")

            # Actualizar la última venta registrada
            last_venta_usd_ccl_cy = venta_usd_ccl_cy

        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        # Esperar 60 segundos antes de la próxima actualización
        time.sleep(60)
