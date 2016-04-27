import RPi.GPIO as GPIO

#Configurar el gpio
GPIO.setmode(GPIO.BOARD)
#Configurar el puerto como entrada pull down
btn=12
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while(1):
		if GPIO.input(btn):
			print('presionado')
			
except KeyboardInterrupt:
    GPIO.cleanup()