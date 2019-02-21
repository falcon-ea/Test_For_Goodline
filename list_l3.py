#!/usr/bin/python3.6
# -----------------------------------
# Program by Evgeny S.
# -----------------------------------
# the quick brown fox jumps over the lazy dog
full_list = input('Введите данные: ')
full_list = full_list.split()
my_set = set(full_list) # преобразование списка в множество
unique_list = list(my_set) # создание нового списка из множества
unique_list.sort()
print('\n'.join(unique_list))