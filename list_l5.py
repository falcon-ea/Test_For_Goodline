#!/usr/bin/python3.6
# -----------------------------------
# Program by Evgeny S.
# -----------------------------------
# the quick brown fox jumps over the lazy dog
from collections import Counter # импортируем модуль Counter из библиотеки collections
full_list = input('Введите данные: ' "\n")
full_list = full_list.split()
full_list.sort() # сортировка списка
c = Counter(full_list)
dict_list = dict.copy(c) # преобразуем результат в словарь
for key in dict_list: # перебор словаря циклом "for"
    print(key, "", dict_list[key])