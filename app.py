from telegram.ext import Updater, MessageHandler, Filters

from Adafruit_IO import Client
 
aio = Client('jatshub2322','aio_RiJG240udsJTJz2f4e4HxHdrt5FV')
 
def jat23(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned on')
  aio.send('major-2-dot-0telebot',22)
 
def jat23(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned off')
  aio.send('major-2-dot-0telebot',23)
 
def jat23(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')
  aio.send('major-2-dot-0',22)
 
def jat23(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')
  aio.send('major-2-dot-0',23)
 
 
def main(bot,update):
  a= bot.message.text.lower()
  
  if a =="turn on light":
    vedh1(bot,update)
  elif a =="turn off light":
    vedh2(bot,update)
  elif a =="turn on fan":
    vedh3(bot,update)
  elif a =="turn off fan":
    vedh4(bot,update) 
     
bot_token =  '1947845258:AAFphKxYcky_wzIMZFvrxNY-Rw-JHd2wJ04'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()   
