# 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
# Пример:
#
# 10 -> 1 2 4 8

N = int(input("Input a number: "))
a = 0
k = 0
while a * 2 <= N:
    a = 2 ** k
    print(a)
    k += 1
