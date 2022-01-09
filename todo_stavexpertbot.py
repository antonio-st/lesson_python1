import random

import telebot
import datetime

token = '5032870475:AAE3py4ep2mWW_sKQg2EiOWf7F9KPFrFQXs'

# type variable of telebot library
bot = telebot.TeleBot(token)

# program help and user commands
HELP = '''
/help - display commands to control the bot
/add - add the task to the list (example: /add 09.01.2022 learning python )
/show  - display all added task on date (example: /show 09.01.2022)
/random  - add a random task fo today
 '''
# declare a dictionary/list
tasks = {}

todayDate = datetime.date.today().strftime("%d.%m.%Y")
print('TODAY : ', todayDate)

randomTasks = ['do morning exercises', 'walk to the Konsomolsky pond', 'an evening walk', 'clean up the yard',
               'learning English']


# add task function
def add_todo(date, task):
    if date in tasks:
        # the day is in the dictionary
        # add the task to the end of the list
        tasks[date].append(task)
        print('You task ', tasks[date], ' recorded on date ', date, '\n')
    else:
        # the date is not in the dictionary
        # create a new record with the date key
        tasks[date] = [task]
        print('You task', '\'', task, '\'', 'recorded on date', date, '\n')


# decorator function to handle all text message: '/help'
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)
    print(message.chat.id, help)


# decorator function to handle all text message: '/add'
@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1]
    task = command[2]
    add_todo(date, task)
    repToChat = 'Task ' + task + ' on ' + date + ' is recorded'
    bot.send_message(message.chat.id, repToChat)


# decorator function to handle all text message: '/random'
@bot.message_handler(commands=['random'])
def randomTask(message):
    if todayDate in tasks:
        print('There are already task today: ')
        bot.send_message(message.chat.id, 'There are already task today: ')
        for task in tasks[todayDate]:
            bot.send_message(message.chat.id, '- ' + task)
            print('- ', task)
    else:
        task = random.choice(randomTasks)
        add_todo(todayDate, task)
        repToChat = 'Task ' + '\'' + task + '\'' + ' on ' + todayDate + ' is recorded'
        bot.send_message(message.chat.id, repToChat)


# decorator function to handle all text message: '/show , /print'
@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    if date in tasks:
        text = date.upper() + '\n'
        bot.send_message(message.chat.id, 'on date: ' + date + '\n')
        print('on date: ', date, '\n')
        for task in tasks[date]:
            # text = text + '- ' + tasks + '\n'
            bot.send_message(message.chat.id, '- ' + task)
            print('- ', task)
    else:
        print('For ', date, 'tasks not found', '\n')
        text = 'For ' + date + ' tasks not found' + '\n'
        bot.send_message(message.chat.id, text)


# constantly access telegram servers
bot.polling(none_stop=True)
