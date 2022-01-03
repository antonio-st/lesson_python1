

# Модифицируйте программу из задания 2 таким образом, чтобы данные не выводились на экран, а сохранялись в
# словарь. Ключами в этом словаре должны быть даты, а значениями - соответствующие им задачи.

print('Task 3')
todoList = {}

dateInput1 = input('Введи дату >> ')
taskReview1 = input('Введи описание задачи >> ')
todoList[dateInput1] = [taskReview1]

dateInput2 = input('Введи дату >> ')
taskReview2 = input('Введи описание задачи >> ')
todoList[dateInput2] = [taskReview2]

dateInput3 = input('Введи дату >> ')
taskReview3 = input('Введи описание задачи >> ')
todoList[dateInput3] = [taskReview3]
print('\n')

print('Полученные задачи на : ', dateInput1, ' \n' , todoList[dateInput1])
print('Полученные задачи на : ', dateInput2, ' \n' , todoList[dateInput2])
print('Полученные задачи на : ', dateInput3, ' \n' , todoList[dateInput3])

