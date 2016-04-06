import RPi.GPIO as GPIO
import time


def blink(led, speed, initial, state):
	actual=time.time()
	if(actual-initial>speed):
		state= not state
		GPIO.output(led, state)
		initial=time.time()
	return (initial, state)

#Variables
led=12		#asignamos el pin 12 a la variable led
speed=1   #tiempo de espera en segundos

#Numeracion de pines de la tarjeta
GPIO.setmode(GPIO.BOARD)

#Configuramos pin 12 como salida
GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

inicial=time.time()
state=1

try:
    while True:
        inicial, state = blink(led,speed,inicial,state)
        print ("hola")
except KeyboardInterrupt:
    GPIO.cleanup()