import datetime
# program help and user commands
HELP = '''
help - print program help
add - add the task to the list (We ask the user for the name of the task)
show  - print all added task
random  - add a random task fo today
 '''
# declare a dictionary/list
tasks = {}
randomTask = 'do morning exercises'
run = True

todayDate = datetime.date.today().strftime("%d %m %Y")
print('TODAY : ', todayDate)


while run:
    command = input('Enter command >> ')
    if command == 'help':
        print(HELP, '\n')
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
    elif command == 'add':
        date = input('Enter the due date for the task>> ')
        task = input('Enter task name >> ')
        if date in tasks:
            # the day is in the dictionary
            # add the task to the end of the list
            tasks[date].append(task)
            print('You task ', tasks[date], ' recorded on date ', date, '\n')
        else:
            # the date is not in the dictionary
            # create a new record with the date key
            tasks[date] = [task]
            print('You task ', tasks[date], ' recorded on date ', date, '\n')
    elif command == 'random':
        if todayDate in tasks:
            print('There are already task today: ')
            for task in tasks[todayDate]:
                print('- ', task)
        else:
            tasks[todayDate] = []
            tasks[todayDate].append(randomTask)
            print('You task ', randomTask, ' recorded on date ', todayDate, '\n')
    elif command == 'exit':
        break
    else:
        print('unknown command !!!', '\n')
        break
print('Program Completed !')
