# -*- coding: utf-8 -*-
import telebot

# Nuestro tokken del bot (el que @BotFather nos dió).
TOKEN = '' 

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
    bot.reply_to(message, "Mi primer Bot")

#Escucha cualquier mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

#Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.set_update_listener(listener) 
#Inicializa el recibir Mensajes
bot.polling()