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
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) #makes buttons to take the size of the phone screen
	itembtn1 = telebot.types.KeyboardButton('Order reports')
	itembtn2 = telebot.types.KeyboardButton('Account')
	itembtn3 = telebot.types.KeyboardButton('Order History')
	itembtn4 = telebot.types.KeyboardButton('Support')
	markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

	bot.reply_to(message, 'Welcome to this bot', reply_markup=markup)
	


@bot.message_handler(func=lambda message: message.text == 'Order reports')
def btn_one_handler(message):
	markup = telebot.types.InlineKeyboardMarkup()
	social1 = telebot.types.InlineKeyboardButton('Instagram', callback_data='instagram')
	social2 = telebot.types.InlineKeyboardButton('Twitter', callback_data='twitter')
	social3 = telebot.types.InlineKeyboardButton('Snapchat', callback_data='snapchat')
	social4 = telebot.types.InlineKeyboardButton('LinkedIn', callback_data='linkedin')
	social5 = telebot.types.InlineKeyboardButton('Facebook', callback_data='facebook')
	markup.add(social1, social2, social3, social4, social5)

	bot.send_message(message.chat.id, 'What social media do you want to order reports?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def handle_callback(call):
	if call.data == 'instagram':
		bot.send_message(call.message.chat.id, 'You want to report Instagram')
	elif call.date == 'twitter':
		bot.send_message(call.message.chat.id, 'You want to report Twitter')
	elif call.data == 'snapchat':
		bot.send_message(call.message.chat.id, 'You want to report Snapchat')
	elif call.data == 'linkedin':
		bot.send_message(call.message.chat.id, 'You want to report LinkedIn')
	elif call.data == 'facebook':
		bot.send_message(call.message.chat.id, 'You want to report Facebook')


@bot.message_handler(func=lambda message: message.chat.text == 'Account')
def btn_two_handler(message):
	bot.send_message(message, 'Your account balance:')

@bot.message_handler(func=lambda message: message.chat.text == 'Support')
def btn_two_handler(message):
	bot.send_message(message, 'Contact reports')


bot.polling()


