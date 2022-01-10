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
print('Start Bot: ', todayDate)




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
    commandOrig = message.text
    if commandOrig == '/add': # a command without date and task has been introduced
        repToChat = '$ Please enter a command in the format:' + '\n' + '/add xx.xx.xxxx your task'
        bot.send_message(message.chat.id, repToChat)
    else:
        command = message.text.split(maxsplit=2)
        date = command[1]
        task = command[2]
        if len(task) <= 3: # short task, less than 3 characters
            repToChat = '$ The task is too short: please enter text more than 3 characters' + '\n'
            bot.send_message(message.chat.id, repToChat)
        else:
            add_todo(date, task)
            repToChat = '$ Task ' + '\'' + task + '\'' + ' on ' + date + ' is recorded'
            bot.send_message(message.chat.id, repToChat)



# decorator function to handle all text message: '/random'
@bot.message_handler(commands=['random'])
def randomTask(message):
    todayDatelocal = datetime.date.today().strftime("%d.%m.%Y")
    if todayDatelocal in tasks:
        print('$ There are already task today: ')
        bot.send_message(message.chat.id, '$ There are already task today: ')
        for task in tasks[todayDatelocal]:
            bot.send_message(message.chat.id, '- ' + task)
            print('- ', task)
    else:
        task = random.choice(randomTasks)
        add_todo(todayDate, task)
        repToChat = '$ Task ' + '\'' + task + '\'' + ' on ' + todayDate + ' is recorded'
        bot.send_message(message.chat.id, repToChat)


# decorator function to handle all text message: '/show , /print'
@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    commandOrig = message.text
    todayDatelocal = datetime.date.today().strftime("%d.%m.%Y")
    if commandOrig in '/show':
        if len(tasks) == 0:
            print('$ For ', todayDatelocal, 'tasks not found', '\n')
            text = '$ For ' + todayDatelocal + ' tasks not found' + '\n'
            bot.send_message(message.chat.id, text)
        else:
            bot.send_message(message.chat.id, '$ You task for the date: ' + todayDatelocal + '\n')
            print('$ You task for the date:  ', todayDatelocal, '\n')
            for task in tasks[todayDatelocal]:
                bot.send_message(message.chat.id, '- ' + task)
                print('- ', task)

    else:
        date = command[1].lower()
        if date in tasks:
            text = date.upper() + '\n'
            bot.send_message(message.chat.id, '$ You task for the date: ' + date + '\n')
            print('$ You task for the date: ', date, '\n')
            for task in tasks[date]:
                # text = text + '- ' + tasks + '\n'
                bot.send_message(message.chat.id, '- ' + task)
                print('- ', task)
        else:
            print('$ For ', date, 'tasks not found', '\n')
            text = '$ For ' + date + ' tasks not found' + '\n'
            bot.send_message(message.chat.id, text)

# decorator function for any text, search for certain words and answer them
@bot.message_handler(content_types=['text'])
def greeting(message):
    if message.text == 'hello'.lower() or 'привет'.lower():
        bot.reply_to(message, text='$ hello '+ message.chat.first_name + ' ! ' + '\n'
                     + '$ to find out the command type /help ')



# constantly access telegram servers
bot.polling(none_stop=True)
