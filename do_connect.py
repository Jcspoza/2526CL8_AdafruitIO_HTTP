# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 26
# Goal : conexion a wifi
# conexion wifi limpia de
# https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/1.access.html
# Version 1.1 : added country + power max +  infos output
# Ver 1.2 added comment true or false for
# 1.4 erro show +error names
# 1.6 -> 1.7 error handling in 'while', not break
# 1.9 Mac showing + conversion to 12 hex digits
# 2.0 led flashing during connection
#
# COMO USAR PARA CONECTARSE A LA RED WIFI
# 1-Guardar este fichero en la PICO W como 'do_connect.py'
# adicionalmente en la PICO W se ha de guardar un fichero
# 'secrets.py' que definira un diccionario secrets['ssid']
# y secrets['password'], nombre huimnao d ela red y su passord rrespectivamente
# 2- importar en el progrma principal
# from do_connect import *
# 3A- ejecutar sin comentarios
# do_connect()
# 3B - ejecutar con comentarios
# do_connect(comment = True)
#

import network, time
from secrets import *
from machine import Pin

def do_connect(ssid=secrets['ssid'],psk=secrets['password'], comment = False):
    
    wStatusDef = {-3:'ERROR_WRONG_PASSWORD',
                  -2:'ERROR_NO_AP_FOUND',
                  -1:'ERROR_CONNECT_FAIL',
                  1:'STAT_CONNECTING',
                  0:'STAT_IDLE',
                  2:'STAT_NO_IP',
                  3:'STAT_Connected'}
    """
    // Return value of cyw43_wifi_link_status
#define CYW43_LINK_DOWN (0)
#define CYW43_LINK_JOIN (1)
#define CYW43_LINK_NOIP (2)
#define CYW43_LINK_UP (3)
#define CYW43_LINK_FAIL (-1)
#define CYW43_LINK_NONET (-2)
#define CYW43_LINK_BADAUTH (-3)
    """
    led = Pin("LED", Pin.OUT)
    
    # Set country to avoid possible errors
    network.country('ES')
    if comment:
        print('"do_connect" function version = 2.0')
        print('Country set to =', network.country())
        print('Connecting to WiFi Network Name:', secrets['ssid'])
    
    # 1- Crea un objeto wireless local area network en modo estacion
    wlan = network.WLAN(network.STA_IF)
    
    # 2- Activa el circuito wifi - tarda unos segundos
    wlan.active(True)
    wlan.config(pm = 0xa11140) # Desactiva el modo de bajo consumo
    
    # 3- se conecta a la red wifi SSID con la clave PASSWORD,
    wlan.connect(ssid, psk)    

    # 4 - hacer un maximo de 10 intentos de conexionm con una espera de 1 seg
    wait = 10
    wStatus = wlan.status()
    while wait > 0 and (wStatus >= 0 and wStatus < 3):
        # 3 posibilidades de salir del bucle: 1->numero de intentos O
        # 2->por error wStatus = -3, -2 o -1
        # 3-> conexion con exito que es wStatus = 3
        wStatus = wlan.status()
        wait -= 1
        if comment:
            print(secrets['ssid'] + ' Wlan Status = '+ wStatusDef[wStatus])
        
        led.on()
        time.sleep(0.25)
        led.off()
        time.sleep(0.25)
        led.on()
        time.sleep(0.25)
        led.off()
        time.sleep(0.25)

    # 4 Compruebo si salio por error, es decir wStatus distinto de 3              
    if wStatus != 3:
        led.on()
        raise RuntimeError('Wifi connection failed-'+ wStatusDef[wStatus])
    else:
        # Conexion exitosa!!
        print('CONNECTED-'+wStatusDef[wStatus])
        ip=wlan.ifconfig()[0] # extrae la direccion ip de PICO W, util para conectar
        led.off()                
        if comment:
            print('Wlan param ip add, mask, gateway & DNS server:', wlan.ifconfig())
            print('id net =', wlan.config('ssid'))
            print('channel =', wlan.config('channel'))
            print('TX power =', wlan.config('txpower'))
            a = wlan.config('mac')
            # MAC Addresses are unique 48-bit hardware number, or 6 bytes
            # MAC is commonly represented as 12 hex digitts
            # To make that conversion consider 'a' as string -> extrtact ead char -> repesent char code in hex
            print(f"Physical-mac add {a[0]:02x}:{a[1]:02x}:{a[2]:02x}:{a[3]:02x}:{a[4]:02x}:{a[5]:02x}")
            print('OUI = 28:CD:C1 => Raspberry Pi Trading Ltd')   
        return ip
