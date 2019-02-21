#!/usr/bin/python3.6
# -----------------------------------
# Program by Evgeny S.
# -----------------------------------
# the quick brown fox jumps over the lazy dog
full_list = input('Введите данные: ')
full_list = full_list.split() # разделение исходной строки на список по пробелам
print('\n'.join(full_list)) # выводим на экран новую строку с новым разделителем