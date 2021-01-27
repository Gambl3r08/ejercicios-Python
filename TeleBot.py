# Bot de Telegram
import telebot
from telebot import types
import time

TOKEN = 'TOKEN'

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'

GRUPO = -XXXXXX

bot = telebot.TeleBot(TOKEN)

# listener
@bot.message_handler(comands=['ayuda'])
def comand_ayuda(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_message(cid, AYUDA)

@bot.message_handler(comands=['info'])
def comand_info(m):
    cid = m.chat.id
    if cid == GRUPO:
        bot.send_message(GRUPO, 'mensaje A')
    else:
        bot.sed_message(cid, 'mensaje B')


def listener(messages): # funcion de llamada
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # el Cid es el identificador del chat, los negativos son grupos y los positivos los usuarios
        if cid > 0:
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text # si 'cid' es positivo usaremos 'm.chat.first_name' para el nombre
        else:
            mensaje = str(m.from_user.first_name) + " [" + str(cid) + "]: " + m.text # si 'cid' es negativo usaremos 'm.from_user.first_name' para nombre
        f = open('log.txt', 'a') # Abrimos nuestro log en modo añadir 'a'
        f.write(mensaje + "\n")
        f.close
        print mensaje
bot.set_update_listener(listener)