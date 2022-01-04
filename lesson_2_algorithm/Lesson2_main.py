#логические операции сравнения

# pasEnter = input ('Enter password >> ')
# pas = 'Python'
# print('Password : ', pasEnter == pas)


# оператор if
pasEnter = input ('Enter password >> ')
pas = 'Python'

if pasEnter == pas:
    print('Access Granted')
elif len(pasEnter) < 6:
    print('The password is too short')
else:
    print('Access Denied')
print ('The program is completed')
