# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.
# Ввод: 1 2 3 4 5
# Вывод: 0
#
# Ввод: 1 5 1 5 1
# Вывод: 2

from time import time
a = list(map(int, input("Введите первый массив:").split()))
start = time()
count = 0
for i in range(1, len(a)-1):
    # print(a[i-1:i+2])
    if a[i] == max(a[i-1:i+2]):
        count += 1
print(count)

print(time()-start)

# mas = [1, 5, 1, 5, 1]
# print(len([i for i in range(1, len(mas)-1) if mas[i] > mas[i - 1] and mas[i + 1]]))

# a = list(map(int, input("Введите первый массив:").split()))
# count = 0
# for i in range(1, len(a)-1):
# if a[i] > a[i-1] and a[i] > a[i+1]:
# count += 1
# print(count)