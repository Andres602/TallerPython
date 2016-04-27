import RPi.GPIO as GPIO

#Configurar el gpio
GPIO.setmode(GPIO.BOARD)
#Configurar el puerto como entrada
btn=12
GPIO.setup(btn, GPIO.IN)

try:
	while(1):
		if GPIO.input(btn):
			print('presionado')
			
except KeyboardInterrupt:
    GPIO.cleanup()