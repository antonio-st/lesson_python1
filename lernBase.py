a = 45
b = 20

# основные арифметические операции

print('a = ', a, 'b = ', b)
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '//', b, '=', a // b)  # Деление без остатка (//)
print(a, '%', b, '=', a % b)  # Деление по модулю (остаток от деления) (%)
print(a, '**', b, '=', a ** b)  # возведение в степень


c = 'Клар у Кары украл кораллы . . .'
print ('Длина строки: ',' ',c,' ', len(c) , ' символ(ов)')

print ('########################## СПИСКИ ########################## ')

listString = ['Hi', 'this', 'is', 'python']
numbers = [1, 2, 3, 4, 5]
data = ['Hi', 'this', 'is', 'python', 28, 18]

summa  = numbers + data
print('Сумма списков: ', summa )

data.append('!')
data.append(8)
print('Добавление данных в конец списка: ', data)

print('*********************************************************************')
showList = listString [1]
print ('Показать 2 элемент списка listString >>', showList)
showListNum = numbers[3] , numbers[4]
print ('Показать 3-4 элемент списка numbers >>', showListNum)

print('*********************************************************************')
stringLength = len(listString)
print('Длина списка listString >>', stringLength)

print('*********************************************************************')

sumStringLength = sum(numbers)
print('Сумма элементов списка numbers >>', sumStringLength)
