import requests
import time
from database import cursor

def get_cotizacion():
    response = requests.get("https://mercados.ambito.com/dolar/informal/variacion", headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
        "Accept-Language": "es-ES,es;q=0.9", 
        "Priority": "u=0, i", 
        "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"", 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"", 
        "Sec-Fetch-Dest": "document", 
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-Site": "none", 
        "Sec-Fetch-User": "?1", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    })
    response.raise_for_status()  # Handle HTTP errors
    
    # Parse the JSON response
    data_usd = response.json()

    return (
        float(data_usd['compra'].replace(',', '.')),
        float(data_usd['venta'].replace(',', '.'))
    )

