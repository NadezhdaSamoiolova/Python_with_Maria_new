# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.

n = int(input("Введите количество элементов арифметической прогрессии: "))
a1 = int(input("Введите первый член арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))


# end_list = []
# for i in range(n):
#     an = a1 + i * d
#     end_list.append(an)
# print(end_list)


# print(list(a1 + i * d for i in range(n)))

def arif_prog(a, b, c):
    end_list = []
    for i in range(a):
        an = b + i * c
        end_list.append(an)
    return end_list


print(arif_prog(n, a1, d))
