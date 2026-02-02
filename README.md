# 2526_CL8 uP: Uso del servicio Adafruit IO con HTTP

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

## Clase 8  (en 2425 Clase 11) - Indice - 90 minutos

- Propósito

- Tutoriales y Programas que vamos a seguir

- Montaje HW

- Introducción Teórica al HTTP (simplificada) 

- Recordar : RTUTP_wifi_nastro_2_0.py, aplicación con HTTP

- Configuración de la cuenta Adafruit y 1ros pasos : feeds y dashboard

- Ejemplo de uso 1: obtener datos / instrucciones desde Internet --> Pico W/2W: leer color neopixel

- Ejemplo de uso 2: subir datos / status desde Pico W/2W --> Internet: enviar temperatura y humedad desde DHT11

- Preguntas sobre la Clase 8
  
  --- fin actualizacion ---

## Propósito

( Sigue desde la clase 7 de 2025 - 2026)

Los montajes HW + SW robóticos enseguida, dentro de la linea de aprendizaje, empiezan a 'trocearse' y se llega a tener de los 2 pedazos, uno de ellos en la 'nube'. Este pedazo en al nube se puede programar desde cero ( como por ejemplo servidor web local) , pero lo normal es que se usen servicios en la nube pre-configurados

En **numastro** lo que hacíamos era preguntar a un servicio en el nube y actuar en consecuencia a la informacion ( solo la mostrábamos en el ejemplo, pero hubiéramos podido tomar decisiones de programa con la informacion.

Mas poderoso es usar **servicios en al nube preconfigurados que permiten subir nuestra propia informacion o enviar comandos o valores** adaptados a nuestro montaje con la PICO W. Vamos a probar uno de estos servicios gratuitos el de [***Adafruit IO***](https://io.adafruit.com/).

## Tutoriales y Programas que vamos a seguir

### Tutoriales resumen

1. Servicio de Adafruit IO - darse de alta y configurar 
   
   1.A) El tutorial de SF 

[8.3 Temperature and Humidity Monitoring via @AdafruitIO &mdash; SunFounder Pico 2 W Starter Kit for Raspberry Pi Pico 2 W documentation](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/iotproject/3-adafruitio.html)

**es confuso** porque mezcla HTTP y MQTT .: NO RECOMIENDO SEGUIRLO, <u>salvo su parte 2 de configuración del servicio de Adafruit IO</u>

1.B) Tutorial en castellano, ver el hasta que cuenta el codigo, que es para un neopixel pero lo realiza de forma diferente

[Raspberry Pi Pico W con Adafruit IO- control de neopixel codigo en micropython](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4)

1.C) y otro Tutorial ( que es mejor que el de SF)

[Upload Sensor Data to Adafruit IO with ESP32 and MicroPython | GPIO.CC Learning](https://gpiocc.github.io/learn/micropython/esp/2020/05/23/martin-ku-upload-sensor-data-to-adafruit-io-with-esp32-and-micropython.html)

o este otro tutorial

2. Explicación de HTTP Una buen y sencilla explicación del HTTP es 

[MicroPython: HTTP GET Requests with ESP32/ESP8266 | Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-http-get-requests-esp32-esp8266/)

4. Repito 2 tutoriales de la Clase 7 que siguen siendo interesantes. 

Tutorial para 'Requests'

[Raspberry Pi Pico W: HTTP GET Requests (MicroPython) | Random Nerd Tutorials](https://randomnerdtutorials.com/raspberry-pi-pico-w-http-requests-micropython/)

Tutorial para tipo de datos JSON devuelto por la mayoría de los servidores

Ver tutorial [Python JSON Data: Una guía con ejemplos](https://www.datacamp.com/es/tutorial/json-data-python)

----

### Tabla resumen de programas

| Programa                                                         | Lenguaje | Objetivo de Aprendizaje | Hw adicional   |
| ---------------------------------------------------------------- | -------- | ----------------------- | -------------- |
| [BMMR_CL19s_wifi_connect_0_1.py](BMMR_CL19s_wifi_connect_0_1.py) | uPy      |                         | no solo PICO W |
|                                                                  | uPY      |                         | solo PICO W    |
|                                                                  | uPy      |                         |                |
|                                                                  | uPY      |                         |                |
|                                                                  | uPy      |                         |                |
|                                                                  | uPy      |                         |                |

### Recomendaciones de estudio despues de la clase

Leer / visualizar los tutoriales indicados

## Montaje HW

Este es el montaje completo, iremos usándolo progresivamente 

La resistencia de pull-up del DHT11 puede tener valores desde 4.7k ohm a 10 k Ohm



![](C:\Users\josec\OneDrive\Documentos\GitHub\2526CL8_AdafruitIO_HTTP\pico_sh1106_npx_DHT11_bb.png)

## Introducción Teórica al HTTP (simplificada)

Sigamos el tutorial 

[MicroPython: HTTP GET Requests with ESP32/ESP8266 | Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-http-get-requests-esp32-esp8266/)

### Recordar : RTUTP_wifi_nastro_2_0.py, aplicación con HTTP

El programas

[RTUTP_wifi_nastro_2_0.py](RTUTP_wifi_nastro_2_0.py)

- El programa en versión 2.0 servirá para otros programas donde necesitemos consultar a un servidor por HTTP : GET , y con pocas modificaciones también para subir datos con POST

Los explicare paso a paso..... y además explicare de forma breve y simplificada:

- Display SH1106 (ver CL7)

- Peticiones API a un servidor por HTTP
  
  Ver tutorial para 'Requests' : [Raspberry Pi Pico W: HTTP GET Requests (MicroPython) | Random Nerd Tutorials](https://randomnerdtutorials.com/raspberry-pi-pico-w-http-requests-micropython/)

- Tipo de datos JSON devuelto por el servidor

Ver tutorial [Python JSON Data: Una guía con ejemplos](https://www.datacamp.com/es/tutorial/json-data-python)

## Configuración de la cuenta Adafruit y 1ros pasos : feeds y dashboard

--> Tutorial en castellano, ver el hasta que cuenta el codigo, que es para un neopixel pero lo realiza de forma diferente

[Raspberry Pi Pico W con Adafruit IO- control de neopixel codigo en micropython](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4)

1. Crear un usuario

2. Suscribir plan básico. El plan básico es Gratis: permite crear hasta 10 feeds y 5 Dashboards. Los feed son el elemento limitante, feed = elemento hw básico , por
   ejemplo, led de 1 color

3. Crear los “feeds” que necesites en función del proyecto, en nuestro proyecto serán 3 = 
   
   + 1 para el neopixel ( no usamos el direccionamiento de cada neopixel individual)
   
   + 2 para temperatura y humedad del sensor DHT 11

4. Componer un Dashboard con los “feeds”, eligiendo el tipo de control o visualizador on/of, slide, aguja, etc

5. Copiar clave, nombre de usuario y nombres de feeds, que necesitaremos en nuestro programa

## Ejemplo de uso 1: obtener datos / instrucciones desde Internet --> Pico W/2W : leer color neopixel

### Test del neopixel

### Configurar el Dashboard en Adafruit IO

### Ejecutar un test GET genérico con Adafruit

### Ejecutar el ejemplo y ver como cambia el color

## Ejemplo de uso 2: subir datos / status desde Pico W/2W --> Internet : enviar temperatura y humedad desde DHT11

---

## Preguntas sobre la Clase 8 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

TO DO :  
