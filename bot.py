import telebot
import os, dotenv

dotenv.load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(bot_token, parse_mode='HTML')

'''
I read your code and i understand different statements like,
message.chat.id == owner: gets the users id to check if the user's id is in the list of owners 
func=lamda m: True: if this condition is true the function under it will run

I also noticed the bot was hosted in a flask app. Is this necessary?

'''

@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, 'Welcome to this bot')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #makes buttons to take the size of the phone screen
itembtn1 = types.KeyboardButton('Order reports')
itembtn2 = types.KeyboardButton('Account')
itembtn3 = types.KeyboardButton('Order History')
itembtn4 = types.KeyboardButton('Support')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

@bot.message_handler(commands=['exit'])
def exit(message):
	bot.reply_to(message, 'Goodbye')
	bot.stop_polling()

bot.polling()


