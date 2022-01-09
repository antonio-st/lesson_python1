import datetime
import random

# program help and user commands
HELP = '''
help - print program help
add - add the task to the list (We ask the user for the name of the task)
show  - print all added task
random  - add a random task fo today
 '''
# declare a dictionary/list
tasks = {}
randomTasks = ['do morning exercises', 'walk to the Konsomolsky pond', 'an evening walk', 'clean up the yard',
               'learning English']
run = True

todayDate = datetime.date.today().strftime("%d %m %Y")
print('TODAY : ', todayDate)

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



while run:
        # help
    command = input('Enter command >> ')
    if command == 'help':
        print(HELP, '\n')
        # show
    elif command == 'show':
        # we specify the date of the task
        # check if there is a date in the dictionary
        # iterate over records by keywords, display tasks
        date = input('Enter a date to display the task list >> ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('For ', date , 'tasks not found', '\n')
        # add
    elif command == 'add':
        date = input('Enter the due date for the task>> ')
        task = input('Enter task name >> ')
        add_todo(date,task) # call the function of adding a task
        # random
    elif command == 'random':
        if todayDate in tasks:
            print('There are already task today: ')
            for task in tasks[todayDate]:
                print('- ', task)
        else:
            task = random.choice(randomTasks)
            add_todo(todayDate, task)
        # exit
    elif command == 'exit':
        break
    else:
        print('unknown command !!!', '\n')
        break
print('Program Completed !')
