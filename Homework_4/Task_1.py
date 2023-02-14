# 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
#
# Пример:
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Input a number of members in set_1: "))
m = int(input("Input a number of members in set_2: "))
set_1 = []
set_2 = []
for i in range(n):
    set_1.append(int(input()))
print(set_1)

for j in range(m):
    set_2.append(int(input()))
print(set_2)
a = set(set_1)
b = set(set_2)

i = sorted(list(a.intersection(b)))
print(i)



##### Решение с семинара #######
# n, m = input().split()
# first = [int(i) for i in input().split()]
# second = [int(j) for j in input().split()]
#
# print(*sorted(set(first).intersection(second)))