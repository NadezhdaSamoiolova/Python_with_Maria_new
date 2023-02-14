# 2 Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к
# заданному числу X.
# Пользователь в первой строке
# вводит натуральное число N –
# количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка # содержит число X
#
# Пример:
#
# 5
# 1 2 3 4 5
# 6
# -> 5

list_n = [int(input()) for _ in range(int(input()))]
print(list_n)

X = int(input("Input a digit: "))
right_num = list_n[0]
for i in list_n:
    if abs(X - i) < abs(X - right_num):
        right_num = i

print(right_num)
