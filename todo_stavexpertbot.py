import telebot

token = '5032870475:AAE3py4ep2mWW_sKQg2EiOWf7F9KPFrFQXs'

# type variable of telebot library
bot = telebot.TeleBot(token)

# program help and user commands
HELP = '''
/help - display commands to control the bot
/add - add the task to the list (We ask the user for the name of the task)
/show  - print all added task
/random  - add a random task fo today
 '''
# declare a dictionary/list
tasks = {}

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
    add_todo(date,task)
    repToChat = 'Task ' + task + ' на '  + date + ' is recorded'
    bot.send_message(message.chat.id, repToChat)

# constantly access telegram servers
bot.polling(none_stop=True)
