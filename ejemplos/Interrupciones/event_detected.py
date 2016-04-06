import Rpi.GPIO as GPIO
import time

#Configurar el gpio
GPIO.setmode(GPIO.BOARD)
#Configurar el puerto como entrada
btn=12
GPIO.setup(btn, GPIO.IN)

#Configuramos para escuchar el franco
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=200)
#Esperamos  por 5 segundos
time.sleep(5)
#Comprobamos si se presiono btn durante ese tiempo
if GPIO.event_detected(channel):
    print('Button pressed')

#Limpiamos los puertos
GPIO.cleanup()