# program help and user commands
HELP = '''
help - print program help
add - add the task to the list (We ask the user for the name of the task)
show  - print all added task
 '''
# declare a dictionary/list
tasks_today = []
tasks_tomorrow = []
task_other = []
run = True

while run:
    command = input('Enter command >> ')
    if command == 'help':
        print(HELP, '\n')
        # if show command is issued : display all list
    elif command == 'show':
        # show the list if it is not empty
        if len(tasks_today) != 0:
            print('Task for today: ', tasks_today, '\n')
        if len(tasks_tomorrow) != 0:
            print('Task for tomorrow: ', tasks_tomorrow, '\n')
        if len(task_other) != 0:
            print('You other task: ', task_other, '\n')
        # add an if loop to write different list
    elif command == 'add':
        dayTask = input('Enter the due date (today/tomorrow/another) for the task >> ')
        if dayTask == 'today':
            task = input('Enter task name >> ')
            tasks_today.append(task)
            print('You task ',  tasks_today[-1], 'on ', dayTask, ' recorded : ', '\n')
        elif dayTask == 'tomorrow':
            task = input('Enter task name >> ')
            tasks_tomorrow.append(task)
            print('You task ', tasks_tomorrow[-1], 'on ', dayTask, ' recorded : ', '\n')
        else:
            task = input('Enter task name>> ')
            task_other.append(task)
            print('You task ', task_other[-1], 'on ', dayTask, ' recorded : ', '\n')
    elif command == 'exit':
        break
    else:
        print('unknown command !!!', '\n')
        break
print('Program Completed !')
