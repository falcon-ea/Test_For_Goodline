#!/usr/bin/python3.6
# -----------------------------------
# Program by Evgeny S.
# -----------------------------------
# the quick brown fox jumps over the lazy dog
full_list = input('Введите данные: ')
full_list = full_list.split()
full_list.sort() # сортировка списка
print('\n'.join(full_list))