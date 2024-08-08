import requests
from datetime import datetime as dt

# Variables para almacenar las últimas cotizaciones
last_compra_usdt_fw = 1350
last_venta_usdt_fw = 1340

# Función para calcular la variación porcentual
def calcular_variacion(actual, anterior):
    if anterior is None:
        return None  # No hay valor anterior para comparar
    return ((actual - anterior) / anterior) * 100

# Obtener datos de la API
response = requests.get("https://criptoya.com/api/fiwind/usdt/ars/0.1")
response.raise_for_status()  # Para manejar errores HTTP

data_usdt = response.json()

# Cotizaciones actuales
compra_usdt_fw = data_usdt['ask']
venta_usdt_fw = data_usdt['bid']
fecha_usdt_fw = dt.now()

# Calcular variaciones
variacion_compra = calcular_variacion(compra_usdt_fw, last_compra_usdt_fw)
variacion_venta = calcular_variacion(venta_usdt_fw, last_venta_usdt_fw)

# Mostrar resultados
print(f"COMPRA USDT: {compra_usdt_fw:.2f}")
print(f"VENTA USDT: {venta_usdt_fw:.2f}")
print(f"Fecha: {fecha_usdt_fw}")
if variacion_compra is not None:
    print(f"Variación COMPRA: {variacion_compra:.2f}%")
else:
    print("No hay variación anterior para COMPRA.")

if variacion_venta is not None:
    print(f"Variación VENTA: {variacion_venta:.2f}%")
else:
    print("No hay variación anterior para VENTA.")

# Actualizar valores anteriores
last_compra_usdt_fw = compra_usdt_fw
last_venta_usdt_fw = venta_usdt_fw

# Calcular precios con margen
compra_usdt_coti = compra_usdt_fw * 0.99
venta_usdt_coti = venta_usdt_fw * 1.01

print(f"COMPRA Coti USDT: {compra_usdt_coti:.2f}")
print(f"VENTA Coti USDT: {venta_usdt_coti:.2f}")
print(data_usdt)
