import telebot

token = '5032870475:AAE3py4ep2mWW_sKQg2EiOWf7F9KPFrFQXs'

# type variable of telebot library
bot = telebot.TeleBot(token)


# decorator function to handle all text message
@bot.message_handler(content_types=['text'])
# message processing function with 2 input parameters : chat.id and message.text
def echo(message):
    run = True
    nameUser = message.text
    word = 'Антон'
    word2 = 'Привет'
    while run:
        if word in nameUser:
            bot.send_message(message.chat.id, 'Ба, знакомые лица !!!')
            print('date/first_name/chat.id/message')
            print(message.date, message.chat.first_name, message.chat.id, message.text)
            break
        if word2 in nameUser:
            bot.send_message(message.chat.id, 'Привет ' + message.chat.first_name + ' !')
            print('date/first_name/chat.id/message')
            print(message.date, message.chat.first_name, message.chat.id, message.text)
        else:
            bot.send_message(message.chat.id, message.chat.first_name + ' you write >> ' + message.text)
            print('date/first_name/chat.id/message')
            print(message.date, message.chat.first_name, message.chat.id, message.text)
        break

# constantly access telegram servers
bot.polling(none_stop=True)
