import RPi.GPIO as GPIO
import time


#Variables
led=12		#asignamos el pin 12 a la variable led
speed=1   #tiempo de espera en segundos

#Numeracion de pines de la tarjeta
GPIO.setmode(GPIO.BOARD)

#Configuramos pin 12 como salida
GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        time.sleep(speed)
        GPIO.output(led, GPIO.LOW)
        time.sleep(speed)
        GPIO.output(led, GPIO.HIGH)
        print ("hola")
except KeyboardInterrupt:
    GPIO.cleanup()