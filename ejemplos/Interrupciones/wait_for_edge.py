import RPi.GPIO as GPIO

#Configurar el gpio
GPIO.setmode(GPIO.BOARD)
#Configurar el puerto como entrada
btn=12
GPIO.setup(btn, GPIO.IN)

#Esperamos por 5 segundos que se presione el btn
press=GPIO.wait_for_edge(btn, GPIO.RISING, timeout=5000)
if press is None:
	print('Timeout')
else
	print('Edge detectado en pin', press)

#Limpiamos lo puertos usados
GPIO.cleanup()			