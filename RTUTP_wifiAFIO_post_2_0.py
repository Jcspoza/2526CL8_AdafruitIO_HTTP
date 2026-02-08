# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase wifi
# Programa: Test de post en Adafruit 
# Hardware platform: Pico W solamente
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# 1.0 : basado en nastro_2_0

from os import uname
# Informative block - start
p_keyOhw = "I2C en GPIO 4&5 = SDA0 & SCL0 400khz"
p_project = "Test POST en adafruit: feed 'dht11temperatura'"
p_version = "1.0"
p_library = "SH1106  @robert-hh + requests"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
import sh1106
from do_connect import *
import requests
import ujson

# 0.0 - Constates y varaibles globales
# para el objeto Display
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

# 0.3 - Constantes para Adafruit IoT
# 'AFIOT_USERNAME' was imported with secrets in module do_connect, use secrets['AFIOT_USERNAME']
# 'AFIOT_KEY' was imported with secrets in module do_connect, use secrets['AFIOT_KEY']
ENCABEZADO = {'X-AIO-Key': secrets['AFIOT_KEY'], 'Content-Type': 'application/json'}
NOMBREFEED = "dht11temperatura"

# 1- Creacion del objeto display,
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

# PROGRAMA PRINCIPAL
# 2- Nos conectamos a Internet
# mostramos por el display que empieza la conexion al wifi
display.text('T.AdafruitIO post', 0, 0, 1)
display.show()
# conectamos la Pico W / 2W a Internet
ip = do_connect()
# si ha sido exitoso mostramos la ip
# ATENCION : este es un progrma simple y no maneja errores de conexion,
# solo la excepcion que muestra do_connect
display.text(ip, 0, 10, 1)
display.show()

# 3- Preguntamos el valor de POST a subir a Tempratura
temperatura = float(input('Di un valor de temperatura entre 0º y 50º'))
Temp2d = {'value': round(temperatura, 2)}
display.text('Temp. = ' + str(round(temperatura, 2)), 0, 20, 1)
display.show()

# 4- Preguntamos en el espacio propio de Adafruti IO con HTTP
display.text('POST..', 0, 30, 1)
display.show()
# 3.1 componemeos en 'end point'
urlAFIO = "https://io.adafruit.com/api/v2/" + secrets['AFIOT_USERNAME'] + "/feeds/" + NOMBREFEED + "/data"
respuesta = requests.post(urlAFIO, headers = ENCABEZADO, data=ujson.dumps(Temp2d))

# 4 - Mostramos la respuesta: formatamos y la mostramos en el display
# 4.1 - primero el status code
codigoRespuesta = respuesta.status_code
display.text(str(codigoRespuesta), 100, 30, 1)
display.show()

# 4.2 Ahora la respuesta en si
# En el caso de un Post - nos interesa unicamente que el codigo fde respeusta sea OK

if codigoRespuesta == 200:
    print(f'Ok de HTTP codigo = {codigoRespuesta}')
else:
    # Tratamiento de errores basico
    print(f'Error de HTTP : {respuesta.reason.decode('utf-8')}')
    display.text('Error de HTTP', 0, 30, 1)
    display.text(respuesta.reason.decode('utf-8'), 0, 40, 1)
    display.show()
