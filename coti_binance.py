
#{"ask":1353.5,"totalAsk":1353.5,"bid":1370,"totalBid":1370,"time":1722008744}

import requests
from datetime import datetime as dt
import time


def get_cotizacion():
    response = requests.get("https://criptoya.com/api/binancep2p/usdt/ars/0.1")
    response.raise_for_status()  # Para manejar errores HTTP

    data_usdt = response.json()

    # Cotizaciones actuales
    return data_usdt['ask'], data_usdt['bid']


# Función para calcular la variación porcentual
def calcular_variacion(actual, anterior):
    if anterior is None:
        return None  # No hay valor anterior para comparar
    return ((actual - anterior) / anterior) * 100


if __name__ == "__main__":
    # Variables para almacenar las últimas cotizaciones
    last_compra_usdt_bnb = None
    last_venta_usdt_bnb = None

    # Bucle para actualizar y calcular cotizaciones
    while True:
        try:
            # Obtener datos de la API
            response = requests.get("https://criptoya.com/api/binancep2p/usdt/ars/0.1")
            response.raise_for_status()  # Para manejar errores HTTP

            data_usdt = response.json()

            # Cotizaciones actuales
            compra_usdt_bnb = data_usdt['ask']
            venta_usdt_bnb = data_usdt['bid']
            fecha_usdt_bnb = dt.now()

            # Calcular variaciones
            variacion_compra = calcular_variacion(compra_usdt_bnb, last_compra_usdt_bnb)
            variacion_venta = calcular_variacion(venta_usdt_bnb, last_venta_usdt_bnb)
            variacion_usdt_bnb = (variacion_compra + variacion_venta) / 2 if variacion_compra is not None and variacion_venta is not None else None

            # Mostrar resultados
            print(f"COMPRA USDT: {compra_usdt_bnb:.2f}")
            print(f"VENTA USDT: {venta_usdt_bnb:.2f}")
            print(f"Fecha: {fecha_usdt_bnb}")

            if variacion_compra is not None:
                print(f"Variación COMPRA: {variacion_compra:.2f}%")
            else:
                print("No hay variación anterior para COMPRA.")

            if variacion_venta is not None:
                print(f"Variación VENTA: {variacion_venta:.2f}%")
            else:
                print("No hay variación anterior para VENTA.")

            if variacion_usdt_bnb is not None:
                print(f"Variación promedio USDT: {variacion_usdt_bnb:.2f}%")

            # Actualizar valores anteriores
            last_compra_usdt_bnb = compra_usdt_bnb
            last_venta_usdt_bnb = venta_usdt_bnb

            # Calcular precios con margen
            compra_usdt_coti = compra_usdt_bnb * 0.99
            venta_usdt_coti = venta_usdt_bnb * 1.01

            print(f"COMPRA Coti USDT: {compra_usdt_coti:.2f}")
            print(f"VENTA Coti USDT: {venta_usdt_coti:.2f}")
        except:
            print("Me rompi")

        # Esperar 60 segundos antes de la próxima actualización
        time.sleep(6)

