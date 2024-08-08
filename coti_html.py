import requests
import time

# Lista para almacenar las cotizaciones anteriores
cotizaciones_anteriores = []

while True:
    try:
        # Hacer una solicitud a la API
        response = requests.get("https://dolarapi.com/v1/ambito/dolares/blue")
        response.raise_for_status()  # Para manejar errores HTTP
        
        # Analizar la respuesta JSON
        data = response.json()
        
        # Acceder a los diferentes valores del JSON
        compra = data.get("compra")
        venta = data.get("venta")
        fecha = data.get("fechaActualizacion")
        
        # Convertir a float
        compra_amb = float(compra)
        venta_amb = float(venta)
        
        # Calcular cotizaciones Coti
        compra_coti = compra_amb - 5
        venta_coti = venta_amb + 5

        # Calcular cotizaciones en EUR
        v_eur_coti = venta_amb * 1.1575
        c_eur_coti = compra_amb * 1.14

        # Guardar cotizaciones actuales en diccionarios
        cotizacion_amb = {
            "compra": compra_amb,
            "venta": venta_amb,
            "fecha": fecha
        }
        
        cotizacion_coti = {
            "compra_usd": compra_coti,
            "venta_usd": venta_coti,
            "compra_eur": c_eur_coti,
            "venta_eur": v_eur_coti,
            "fecha": fecha
        }

        # Crear contenido HTML
        html_content = f"""
        <html>
        <head>
            <title>Cotizaciones de Dólar</title>
        </head>
        <body>
            <h1>Cotizaciones de Dólar y Euro</h1>
            <table border="1">
                <tr>
                    <th>Tipo</th>
                    <th>Compra USD</th>
                    <th>Venta USD</th>
                    <th>Compra EUR</th>
                    <th>Venta EUR</th>
                    <th>Fecha</th>
                </tr>
                <tr>
                    <td>Ambito</td>
                    <td>{cotizacion_amb['compra']}</td>
                    <td>{cotizacion_amb['venta']}</td>
                    <td>N/A</td>
                    <td>N/A</td>
                    <td>{cotizacion_amb['fecha']}</td>
                </tr>
                <tr>
                    <td>Coti</td>
                    <td>{cotizacion_coti['compra_usd']}</td>
                    <td>{cotizacion_coti['venta_usd']}</td>
                    <td>{cotizacion_coti['compra_eur']}</td>
                    <td>{cotizacion_coti['venta_eur']}</td>
                    <td>{cotizacion_coti['fecha']}</td>
                </tr>
            </table>
        </body>
        </html>
        """

        # Guardar el contenido HTML en un archivo
        with open("cotizaciones.html", "w") as file:
            file.write(html_content)

        print("Página HTML actualizada con las últimas cotizaciones.")

        # Guardar cotizaciones
        cotizaciones_anteriores.append(cotizacion_amb)

        # Generar alerta si hay una baja mayor a 15 en compra o venta
        if len(cotizaciones_anteriores) > 1:
            compra_anterior = cotizaciones_anteriores[-2]["compra"]
            venta_anterior = cotizaciones_anteriores[-2]["venta"]
            
            if cotizacion_amb["compra"] < compra_anterior - 15:
                print("¡Alerta! Baja mayor a 15 en la cotización de compra.")
            if cotizacion_amb["venta"] < venta_anterior - 15:
                print("¡Alerta! Baja mayor a 15 en la cotización de venta.")
        
        # Esperar 60 segundos antes de la siguiente solicitud
        time.sleep(60)
        
    except requests.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        time.sleep(60)
    except ValueError as ve:
        print(f"Error al convertir datos: {ve}")
        time.sleep(60)
