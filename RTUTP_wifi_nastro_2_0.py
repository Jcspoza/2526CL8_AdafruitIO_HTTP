# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase wifi
# Programa: Test de conexion a wifi y hacer un get numero astronautas en espacio
# Hardware platform: Pico W solamente
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# 1.0 -> 1.1 visualizacion mejorada
# 2.0 manejo errores HTTP

from os import uname
# Informative block - start
p_keyOhw = "I2C en GPIO 4&5 = SDA0 & SCL0 400khz"
p_project = "Conexion a wifi, GET numero astronautas + manejo errores HTTP"
p_version = "2.0"
p_library = "SH1106  @robert-hh + requests"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
import sh1106
from do_connect import *
import requests

# 0.0 - Constates y varaibles globales
# para el objeto Display
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

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
display.text('Test Wifi n astro', 0, 0, 1)
display.show()
# conectamos la Pico W / 2W a Internet
ip = do_connect()
# si ha sido exitoso mostramos la ip
# ATENCION : este es un progrma simple y no maneja errores de conexion,
# solo la excepcion que muestra do_connect
display.text(ip, 0, 10, 1)
display.show()

# 3- Preguntamos a una web sobre los astronautas en el espacio con HTTP
display.text('GET...', 0, 20, 1)
display.show()
# url = "http://api.open-notify.org/astros.json" # Cuantos humanos hay en el espacio ahora?
url = "http://api.open-notify.org/astros.json"
endPoint = url
respuesta = requests.get(endPoint)
# ATENCION : este es un programa simple y no maneja errores de servidor HTTP
# 4 - Mostramos la respuesta: formatamos y la mostramos en el display
# 4.1 - primero el status code
codigoRespuesta = respuesta.status_code
display.text(str(codigoRespuesta), 100, 20, 1)
display.show()

# 4.2 Ahora la respuesta en si
# la respuesta viene en un formato tipo JSON que convertimos a dicionario Python
# con el metodo ya incluido en requests 'json'
# Para volcar la respuesta hay que conocer su estructura -> ver la ayuda de la API

if codigoRespuesta == 200:
    display.text(str(respuesta.json()['number']), 0, 30, 1)
    display.text('astronautas', 25, 30, 1) # dejo espacio para 3 digitos
    display.text('1 '+ respuesta.json()['people'][0]['name'], 0, 40, 1)
    display.text('2 '+ respuesta.json()['people'][1]['name'], 0, 50, 1)
    display.show()
else:
    display.text('Error de HTTP', 0, 30, 1)
    display.text(respuesta.reason.decode('utf-8'), 0, 40, 1)
    display.show()
