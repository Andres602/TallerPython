#!/usr/bin/python
import RPi.GPIO as GPIO

#Variables
led=12 	#Led
fc=0.5 	#Frecuencia (Hz)
dc=1 	#Duty cicle (0.0 <= dc <= 100.0)

#Numeracion de pines de la tarjeta
GPIO.setmode(GPIO.BOARD)
#Configuramos pin 12 como salida
GPIO.setup(led, GPIO.OUT)

#Creamos un PWM
p = GPIO.PWM(led, fc)
#Iniciamos el PWM
p.start(dc)
raw_input('Presiona Enter para parar:') 
#Detenemos el PWM
p.stop()
#Limpiamos los puertos
GPIO.cleanup()