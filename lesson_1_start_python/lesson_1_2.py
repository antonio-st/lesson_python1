#!/usr/bin/env python
# -*- coding: utf-8 -*-

#СЛОВАРИ

#задаем словарь стран
countries ={
    'Африка': ['Египет', 'Буркина Фасо', 'ЮАР'],
    'Азия': ['Китай', 'Тайланд', 'Индонезия'],

}
#выводим страны из словаря
print('\n')
africa = countries['Африка']
print(africa)

#выводим страны из словаря (альтернативно)
print('\n')
africa_key = 'Африка'
print(countries[africa_key])

#добавляем элемент в словарь
print('\n')
print('#добавляем элемент в словарь')
countries ['Европа'] = ['Сербия', 'Болгария', 'Италия']
print(countries)
print('Страны Европы в словаре : ', countries['Европа'])

#добавляем элемент в конец списка из словаря
print('\n')
print('#добавляем элемент "Эфиопия" в конец списка из словаря')

africa.append('Эфиопия')
print('Обновленный список \n',africa)
print('Обновленный словарь \n', countries)
# длина списка в словаре
print('\n')
print('длина списка Европа в словаре>> ', len(countries['Африка']))


#добавим к списку новый континент / страну введеные пользователем
print('\n')
print('#добавим к списку новый континент / страну введеные пользователем')

addVocContinent = input('введи название континента >> ')
addVocCountry1 = input ('введи название страны 1 >> ')
addVocCountry2 = input ('введи название страны 2 >> ')
addVocCountry3 = input ('введи название страны 3 >> ')

countries[addVocContinent] = [addVocCountry1,addVocCountry2,addVocCountry3]

print('Обновленный словарь \n', countries)
