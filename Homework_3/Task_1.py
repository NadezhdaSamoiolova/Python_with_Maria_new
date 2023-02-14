# 1 Требуется вычислить, сколько раз
# встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# Пример:
#
# 5
# 1 2 3 4 5
# 3
# -> 1

### _____ My realiation ______ ####
N = int(input("Input a nuber: "))
list_n = []
for i in range(N):
    list_n.append(int(input()))

X = int(input("Input a digit: "))
# sum_res = 0
# for k in list_n:
#     if X == k:
#         sum_res += 1
# print(sum_res)

print(sum(1 for k in list_n if X == k))

### _____ Realisation from Seminar ______ ####

list_n = [int(input()) for _ in range(int(input()))]
print(list_n.count((int(input()))))
