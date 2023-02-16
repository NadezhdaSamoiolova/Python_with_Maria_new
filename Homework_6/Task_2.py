# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import numpy as np

n = int(input("Введите количество элементов списка: "))
a = int(input("Введите минимальное значение в списке: "))
b = int(input("Введите максимальное значение в списке: "))

your_list = list(np.random.randint(a, b, n))
print("Ваш список: ", your_list)


#
# lst_min = min(your_list)
# lst_max = max(your_list)
# for i in range(len(your_list)):
#     if lst_min < your_list[i] < lst_max:
#         print(i, end='')
#


def indexes(lst):
    lst_min = min(lst)
    lst_max = max(lst)
    for i in range(len(lst)):
        if lst_min < lst[i] < lst_max:
            print(i, end=' ')


indexes(your_list)
