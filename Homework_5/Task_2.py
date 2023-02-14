# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только
# +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 1:
        return a + 1
    else:
        x = b - 1
        return 1 + sum(a, x)


print(sum(5, 6))

#### Solution of Maria

# def f(a, b):
#     if b == 0:
#         return a
#     return f(a + 1, b - 1)
#
#
# n = int(input())
# m = int(input())
# print(f(n, m))
