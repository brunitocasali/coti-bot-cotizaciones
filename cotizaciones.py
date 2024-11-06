from datetime import datetime
import time

import api_fiwind
import dolar_blue_cy
import coti_binance
import dolar_ccl_cy
import dolar_amb_mep
import api_buenbit
import api_tiendacry
import api_argenbtc
import api_pluscrypto
import api_bybit
import api_mep
import api_ccl



import database



COTIZACIONES = {
    "Dolar Blue": dolar_blue_cy.get_cotizacion,
    "fiwind": api_fiwind.get_cotizacion,
    "binance": coti_binance.get_cotizacion,
    "ccl": dolar_ccl_cy.get_cotizacion,
    "mep": dolar_amb_mep.get_cotizacion,
    "buenbit": api_buenbit.get_cotizacion,
    "tiendacry": api_tiendacry.get_cotizacion,
    "argenbtc": api_argenbtc.get_cotizacion,
    "pluscrypto": api_pluscrypto.get_cotizacion,
    "bybit": api_bybit.get_cotizacion,
    "mep": api_mep.get_cotizacion,
    "ccl": api_ccl.get_cotizacion,
}

# NO TOCAR ABAJO DE ESTA LINEA

def main():
    last_compra = {
        k: None for k in COTIZACIONES
    }
    last_venta = {
        k: None for k in COTIZACIONES
    }

    while True:
        for portal, get_cotizacion in COTIZACIONES.items():
            try:
                date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(date_time)
                compra, venta = get_cotizacion()
                print(datetime.now(), portal, compra, venta)
                
                if last_compra[portal] and last_venta[portal]:
                    variacion_compra = compra / last_compra[portal] - 1
                    variacion_venta = venta / last_venta[portal] - 1
                    variacion = (variacion_compra + variacion_venta) / 2
                    database.cursor.execute("INSERT INTO COTI_USD (PORTAL, FECHA, COMPRA, VENTA, VARIACION) VALUES(?, ?, ?, ?, ?)", (portal, date_time, compra, venta, variacion))
                    database.connection.commit()

                last_compra[portal], last_venta[portal] = compra, venta
            except Exception as e:
                print(e)

        time.sleep(60)

if __name__ == "__main__":
    main()
