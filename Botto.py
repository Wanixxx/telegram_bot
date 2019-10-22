#Стандартный бот, который отвечает тем же текстом, что ты и написал
# coding=UTF-8
import TestBOT
import telebot

bot = telebot.TeleBot(TestBOT.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	#bot.send_message(message.chat.id, message.text) #Отвечает смс на смс
	#bot.reply_to(message, message.text) #Пересылая твоё смс он отвечает на него

	#if __name__ == '__main__':
	if message.text.lower() == 'привет' or message.text.lower() == 'здорова':
		bot.send_message(message.chat.id, 'Привет, мой друг!')
	elif message.text.lower() == 'как у тебя дела?' or message.text.lower() == 'как дела?' or message.text.lower() == 'как сам?':
		bot.send_message(message.chat.id, 'У меня всё хорошо, я тружусь. Как твои дела?)')
	elif message.text.lower() == 'пока' or message.text.lower() == 'я погнал, давай':
		bot.send_message(message.chat.id, 'Пока, жду тебя обратно!')
	elif message.text.lower() == 'скинь стикер':
		bot.send_sticker(message.chat.id, 'CAADAgADBAADwsa9FfvnokueuZsvFgQ')
	elif message.text.lower() == 'отлично' or message.text.lower() == 'отлично)':
		bot.send_sticker(message.chat.id, 'CAADAgADBAADwsa9FfvnokueuZsvFgQ')
	elif message.text == 'Какой символ у Алана Волкера?' or message.text == 'Какой символ у Alana?':
		bot.send_sticker(message.chat.id, 'CAADBAADAgcAAtoAAWIHmBJSAAHZkZpdFgQ')
	elif message.text == 'Какой символ у Marshmello?':
		bot.send_sticker(message.chat.id, 'CAADBAADFQcAAtoAAWIHLjwIVebn0dUWBA')

@bot.message_handler(content_types=['sticker'])	
def sticker_id(message):
	print(message)

bot.polling()#none_stop=True