# program help and user commands
HELP = '''
help - print program help
add - add the task to the list (We ask the user for the name of the task)
show  - print all added task
 '''
# declare a dictionary/list
tasks = []
run = True

while run:
    command = input ('Enter command >> ')
    if command == 'help':
        print(HELP, '\n')
    elif command == 'show':
        print(tasks, '\n')
    elif command == 'add':
        task = input('Enter task name >> ')
        tasks.append(task)
        print('You task ', tasks[-1], ' recorded : ', '\n')
    elif command == 'exit':
        break
    else:
        print('unknown command !!!', '\n')
        break
print('Program Compleated !')
