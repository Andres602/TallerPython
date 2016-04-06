#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#Variables
led=12 	#Led
fc=50 	#Frecuencia (Hz)

#Numeracion de pines de la tarjeta
GPIO.setmode(GPIO.BOARD)
#Configuramos pin 12 como salida
GPIO.setup(led, GPIO.OUT)


p = GPIO.PWM(led, fc) 	#Configuramos el PWM
p.start(0) 				#Iniciamos el PWM
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
#Detenemos el PWM
p.stop()
#Limpiamos los puertos
GPIO.cleanup()