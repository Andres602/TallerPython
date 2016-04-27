# -*- coding: utf-8 -*-
import telebot
from telebot import types
import RPi.GPIO as GPIO

#Variables
led=12		#asignamos el pin 12 a la variable led
TOKEN = '' # Nuestro tokken del bot

#Numeracion de pines de la tarjeta
GPIO.setmode(GPIO.BOARD)

#Configuramos pin 12 como salida
GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

#Crea un bot y le asingan el token
bot = telebot.TeleBot(TOKEN)

#---------Monitorear los Mensajes desde la terminal-------------
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
	for m in messages: # Por cada dato 'm' en el dato 'messages'
		cid = m.chat.id # Almacenaremos el ID de la conversación.
		if m.content_type == 'text':
			print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start
		else:
			print ("[" + str(cid) + "]: " + m.content_type)
#----------------------------------------------------------------

#Escucha el comando start o help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Este bot sirve para encender o apagar un LED", reply_markup=markup)

#Escucha cualquier mensaje parecido a ON
@bot.message_handler(regexp="ON");
def on_led(message):
    bot.reply_to(message, "Led Encendido")
    GPIO.output(led, GPIO.HIGH)

#Escucha cualquier mensaje parecido a OFF
@bot.message_handler(regexp="OFF");
def on_led(message):
    bot.reply_to(message, "Led Apagado")
    GPIO.output(led, GPIO.LOW)    

#--------------Teclado---------------------------
markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard = True)
markup.add('Si', 'No')

try:
	#Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
	bot.set_update_listener(listener) 
	#Inicializa el recibir Mensajes
	bot.polling()
except KeyboardInterrupt:
	pass
GPIO.cleanup()
print("Bot Apagado")  