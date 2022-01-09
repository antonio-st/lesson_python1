import telebot

token = '5032870475:AAE3py4ep2mWW_sKQg2EiOWf7F9KPFrFQXs'

# type variable of telebot library
bot = telebot.TeleBot(token)


# decorator function to handle all text message
@bot.message_handler(content_types=['text'])
# message processing function with 2 input parameters : chat.id and message.text
def echo(message):
    bot.send_message(message.chat.id, message.chat.first_name + ' you write >> ' + message.text)


# constantly access telegram servers
bot.polling(none_stop=True)
