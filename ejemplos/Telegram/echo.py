# -*- coding: utf-8 -*-
import telebot

# Nuestro tokken del bot (el que @BotFather nos dió).
TOKEN = '' 

#Crea un bot y le asingan el token
bot = telebot.TeleBot(TOKEN)

#Escucha el comando start o help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Mi primer Bot")

#Escucha cualquier mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

#Inicializa el recibir Mensajes
bot.polling()