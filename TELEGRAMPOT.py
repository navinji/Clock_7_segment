import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def handle(msg):
    chat_id=msg["chat"]["id"]
    command=msg["text"]
    print('Got command:',command)

    if command == 'on':
        bot.sendMessage(chat_id,"LED on")
        GPIO.output(11,GPIO.HIGH)
    elif command=='off':
        bot.sendMessage(chat_id,"LED off")
        GPIO.output(11,GPIO.LOW)
    elif command == 'stop':
        exit()

try:
    bot = telepot.Bot('5767261316:AAHjmoJTk7DmoT24LVan9fo9QKvNVr7GMr4')
    bot.message_loop(handle)
    print('I am listning..')
    while 1:
        time.sleep(10)
except TelegramError:
   print ('')
