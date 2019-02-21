#!/usr/bin/python3.6
# -----------------------------------
# Program by Evgeny S.
# -----------------------------------
# the quick brown fox jumps over the lazy dog
from collections import Counter # импортируем модуль Counter из библиотеки collections
full_list = input('Введите данные: ')
full_list = full_list.split()
full_list.sort() # сортировка списка
c = Counter(full_list)
dict_list = dict.copy(c) # преобразуем результат в словарь
for key in dict_list: # перебор словаря циклом "for"
    print(key, "", dict_list[key])

# альтернативное решение: (не знаю зачем его здесь привожу, т.к. есть более простое решение,
# но, т.к. я много времени потратил на него, решил тоже представить его Вашему вниманию)
# i = len(full_list) - len(full_list) * 2 # вычисляем первоначальное значение счетчика
# while i <= -1: # счетчик остановится на последнем элементе включительно
#     i_value = (dict_list[full_list[i]]) # получение из словаря значения, соответствующего данной итерации
#     print(full_list[i] + ' ' + str(i_value))
#     print(dict_list.get(full_list[i]))
#     i += 1