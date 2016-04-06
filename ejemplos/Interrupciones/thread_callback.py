#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#Callbacks
def callback_uno(channel):
	print('Callback uno')

def callback_dos(channel):
	print('Callback dos')

#Variables
led=12 	#asignamos el pin 12 a la variable led
btn=13 	#asignamos el pin 13 a la variable btn
speed=1 #tiempo de espera en segundos

#Numeracion de pines de la tarjeta
GPIO.setmode(GPIO.BOARD)

#Configuramos pin 12 como salida
GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)
#Configurar el pin 13 como entrada
GPIO.setup(btn, GPIO.IN)

#Configuramos las callback
#Escuchar franco de subida
GPIO.add_event_detect(btn, GPIO.RISING, bouncetime=200) 	 	
#Asignamos Callback uno a btn
GPIO.add_event_callback(btn, my_callback_one)	
#Asignamos Callback dos a btn
GPIO.add_event_callback(btn, my_callback_two)	

try:
    while True:
        time.sleep(speed)
        GPIO.output(led, GPIO.LOW)
        time.sleep(speed)
        GPIO.output(led, GPIO.HIGH)
        print ("hola")
except KeyboardInterrupt:
	pass

print('Limpiando puertos')
GPIO.cleanup()
print('Cerrando')