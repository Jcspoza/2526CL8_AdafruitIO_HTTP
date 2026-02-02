# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2025 - 12 - 29
# Goal : neopixel x 8 -> basic test
# Learning Target : control y test de neopixel x 8
# Ref : https://dmccreary.github.io/learning-micropython/basics/05-neopixel/

from machine import Pin
from time import sleep
from neopixel import NeoPixel

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External neopixel on GPIO15"
p_project = "Neopixel-test 3 colors BRIGHT MEDIUM"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# El brillo es un valor de 0 a 255, usaremos el mismo para cada color
# Cada pixel se define por 3 valores de color en el orden RGB
# es decir (255, 0, 0) = rojo ; (0, 255, 0) = verde ; (0, 0, 255) = azul;
# y todas las combinaciones de valores desde 0 a 255 en cada color

BRILLO = 127 # brillo medio
# Aqui definimos la espera entre cada cambio a segundos
ESPERA = 2

# 1- Crea el objeto neopixel
NUMERO_PIXELS = 8
NEOPIXEL_PIN = 14
tira = NeoPixel(Pin(NEOPIXEL_PIN),NUMERO_PIXELS )

# 2.1- configuramos pizarra delcontrolador a rojo 
tira[0] = (BRILLO, 0, 0)
tira.write()
sleep(ESPERA)
tira[1] = (0, BRILLO, 0)
tira.write()
sleep(ESPERA)
tira[2] = (0,0, BRILLO)
tira.write()
sleep(ESPERA)
tira[3] = (BRILLO, BRILLO, 0)
tira.write()
sleep(ESPERA)
tira[4] = (0, BRILLO, BRILLO)
tira.write()
sleep(ESPERA)
tira[5] = (BRILLO,0, BRILLO)
tira.write()
sleep(ESPERA)
tira[6] = (50, 50, 50)
tira.write()
sleep(ESPERA)
tira[7] = (BRILLO, BRILLO, BRILLO)
tira.write()
sleep(ESPERA)


# 2.4- configuramos pizarra delcontrolador a todos apagados
tira.fill((0, 0, 0))

# 3.4 Volcamso pizarra de ucontrolador a la del dispositivo y Fin
tira.write()

