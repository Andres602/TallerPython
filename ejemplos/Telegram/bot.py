# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import glob, os
from random import randint

path='imagenes'
os.chdir(path)

 
TOKEN = '164590402:AAG1iF3H5pn5nYIGFxjSx8X7-kL0N4fbf-4' # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
 
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # Almacenaremos el ID de la conversación.
        if m.content_type == 'text':
        	print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
        else:
        	print "[" + str(cid) + "]: " + m.content_type 
 
#Envia una foto de las guardadas
@bot.message_handler(commands=['foto'])
def handle_start_help(m):
	cid = m.chat.id
	name_image = randimage()
	photo = open(name_image +'.jpg', 'rb')
	bot.send_photo(cid, photo)
	#bot.send_photo(cid, "FILEID")

#Guarda la foto que recibe
@bot.message_handler(content_types=['photo'])
def handle_docs_audio(m):
	file_info = bot.get_file(m.photo[2].file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	name_image = getname()
	with open(name_image+'.jpg', 'wb') as new_file:
		new_file.write(downloaded_file)

def getname():
	files=[] #Lista para los archivos
	num=0
	for file in glob.glob("*.jpg"): #Busca archivos con ese nombre en particular
		num=num+1
	name = 'IMG_' + str(num).zfill(3)
	return name

def randimage():
	files=[] #Lista para los archivos
	num=-1
	for file in glob.glob("*.jpg"): #Busca archivos con ese nombre en particular
		num=num+1
	name = 'IMG_' + str(randint(0,num)).zfill(3)
	return name



#cuenta el numero de archivos jpg en el folder
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.