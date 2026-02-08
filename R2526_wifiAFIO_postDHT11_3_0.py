# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase wifi
# Programa: Test de post en Adafruit - Humedad
# Hardware platform: Pico W solamente
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# 1.0 : basado en nastro_2_0
# 2.0 basado en RTUT_wifiAFIO_postHT
# 3.0 : manejo errores + mostran en display


from os import uname
# Informative block - start
p_keyOhw = "I2C en GPIO 4&5 = SDA0 & SCL0 400khz + DHT11 en GPIO15"
p_project = "Enviar datos DHT11 a AdafruitIO + manejo y ver error: feed 'dht11humedad' y 'dht11temperatura'"
p_version = "3.0"
p_library = "SH1106  @robert-hh + requests + DHT11"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
import sh1106
from do_connect import *
import requests
import ujson
import dht
from time import sleep
import errno

# 0.0 - Constates y varaibles globales
# para el objeto Display
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

# 0.3 - Constantes para Adafruit IoT
# 'AFIOT_USERNAME' was imported with secrets in module do_connect, use secrets['AFIOT_USERNAME']
# 'AFIOT_KEY' was imported with secrets in module do_connect, use secrets['AFIOT_KEY']
ENCABEZADO = {'X-AIO-Key': secrets['AFIOT_KEY'], 'Content-Type': 'application/json'}
NOMBREFEEDH = "dht11humedad"
NOMBREFEEDT = "dht11temperatura"

# 1.1 - Creacion del objeto display,
# primero el objeto i2c para comunicarnos con el display
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
# luego el display
display = sh1106.SH1106_I2C(WIDTH,
                            HEIGHT,
                            i2c,
                            res = None,
                            addr = 0x3c,
                            rotate = 0) # valores 0, 90, 180, 270
display.sleep(False)
display.fill(0) # toda la pantalla en negro
# Fin de la inicializacion del display

# 1.2 Crea el objeto DHT11 sensor
sensor = dht.DHT11(Pin(15))

# PROGRAMA PRINCIPAL
# 2- Nos conectamos a Internet
# mostramos por el display que empieza la conexion al wifi
display.text('Conex. internet', 0, 0, 1)
display.show()
# conectamos la Pico W / 2W a Internet
ip = do_connect()
# si ha sido exitoso mostramos la ip
# ATENCION : este es un progrma simple y no maneja errores de conexion,
# solo la excepcion que muestra do_connect
display.text(ip + ' OK', 0, 10, 1)
display.show()
sleep(2)

while True:
    print('Nuevo POST')
    display.fill(0)
    display.text('T.Adaf.IO post', 0, 0, 1)
    display.text(ip, 0, 10, 1)
    try:
        # 3- LEER EL SENSOR
        sensor.measure()
        # lee valores
        Temperatura = sensor.temperature()  # In Celsius
        Humedad = sensor.humidity()      # In Percent
        print(f"Temperatura: {Temperatura:02d}°C   Humedad: {Humedad:02d}%")
        display.text('Hum% = ' + str(Humedad), 0, 20, 1)
        display.text('Temp. = ' + str(round(Temperatura, 2)), 0, 30, 1)
        display.show()
        
        Temp = {'value': Temperatura}
        
        # 4 - POST DE HUMEDAD
        display.text('POST..Hum', 0, 40, 1)
        display.show()
        # 4.1 componemos en 'end point' para humedad
        urlAFIOh = "https://io.adafruit.com/api/v2/" + secrets['AFIOT_USERNAME'] + "/feeds/" + NOMBREFEEDH + "/data"
        Hum = {'value': Humedad} # configura la carga a enviar
        respuestaH = requests.post(urlAFIOh, headers = ENCABEZADO, data=ujson.dumps(Hum))
        # 4.2 - Mostramos la respuesta: formatamos y la mostramos en el display
        # primero el status code
        codigoRespuestaH = respuestaH.status_code
        print(f'Codigo de respuesta a post Humedad = {codigoRespuestaH}')
        display.text(str(codigoRespuestaH), 100, 40, 1)
        display.show()
        
        # 4.3 Ahora la respuesta de la que solo interesa
        # codigo de respuesta pòrtque es un POST
        if codigoRespuestaH != 200:
            print("Error de HTTP en post Humedad")
            print(respuestaH.reason.decode('utf-8'))
#             display.fill(0)
#             display.text('T.Adaf.IO post', 0, 0, 1)
#             display.text(ip, 0, 10, 1)
#             display.text('Error de HTTP', 0, 50, 1)
#             display.show()
            sleep(0.5) # Evita bucles de error rápidos

        # 5- POST DE TEMPERATURA
        display.text('POST..Tem', 0, 50, 1)
        display.show()
        # 5.1 componemos el 'end point' DE TEMPERATURTA
        urlAFIOt = "https://io.adafruit.com/api/v2/" + secrets['AFIOT_USERNAME'] + "/feeds/" + NOMBREFEEDT + "/data"
        Temp = {'value': Temperatura} # configura la cartga a enviar
        respuestaT = requests.post(urlAFIOt, headers = ENCABEZADO, data=ujson.dumps(Temp))
        # 5.2 - Mostramos la respuesta: formatamos y la mostramos en el display
        # primero el status code
        codigoRespuestaT = respuestaT.status_code
        print(f'Codigo de respuesta a post temperatura = {codigoRespuestaT}')
        display.text(str(codigoRespuestaT), 100, 50, 1)
        display.show()
        
        # 5.3 Ahora la respuesta de la que solo interesa
        # codigo de respuesta pòrtque es un POST     
        if codigoRespuestaT != 200:
            print("Error de HTTP en post Temperatura")
            print(respuestaT.reason.decode('utf-8'))
#             display.fill(0)
#             display.text('T.Adaf.IO post', 0, 0, 1)
#             display.text(ip, 0, 10, 1)
#             display.text('Error de HTTP', 0, 50, 1)
#             display.show()
            sleep(0.5) # Evita bucles de error rápidos
            
        sleep(60)   

    except OSError as e:
        print(f"Error bruto {e} - Error codigo {e.errno}")
        if e.errno == 110:
            print('Error de tieme out en lectura de sensor')
            display.fill_rect(0, 10, 128, 8, 0)
            display.text('Error: DHT11', 0, 10, 1)
            display.show()
            
        if e.errno == -2:
            print('Error en orden request ')
            display.fill_rect(0, 10, 128, 8, 0)
            display.text('Error: Requests', 0, 10, 1)
            display.show()
            
        sleep(0.5) # Evita bucles de error rápidos
        
    except KeyboardInterrupt:
        print("Interrupcion de teclado")
        display.fill(0)
        display.text('Parado x teclado', 0, 0, 1)
        display.show()
        break
    
