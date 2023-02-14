# 2. В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
#
# Пример:
#
# 4 -> 1 2 3 4
# 9

N = int(input("Сколько кустов: "))
berry = []
for i in range(N):
    berry.append(int(input("Сколько ягод на каждом кусте: ")))
print(berry)


max_sum_berry = 0
for j in range(len(berry)):
    sum_berry = 0
    if j == N - 1:
        sum_berry = berry[j] + berry[0] + berry[j - 1]
    else:
        sum_berry = berry[j] + berry[j + 1] + berry[j - 1]

    if sum_berry > max_sum_berry:
        max_sum_berry = sum_berry
        j += 1
print(max_sum_berry)

#### Эксперименты с функциями
# def count_berries(bush_amount, berry_amount):
#     max_sum_berry = 0
#     for j in range(len(berry_amount)):
#         sum_berry = 0
#         if j == bush_amount - 1:
#             sum_berry = berry_amount[j] + berry_amount[0] + berry_amount[j - 1]
#         else:
#             sum_berry = berry_amount[j] + berry_amount[j + 1] + berry_amount[j - 1]
#
#         if sum_berry > max_sum_berry:
#             max_sum_berry = sum_berry
#             j += 1
#     print(max_sum_berry)
#
#
# count_berries(4, [1, 2, 3, 4])


##### Решение с семинара
# 4 1 2 3
# 4 2 1 3

# n = int(input())
# bushes = [int(i) for i in input().split()]
# bush_max = 0
#
# for i in range(-1, n - 1):
#     bush_sum = bushes[i - 1] + bushes[i] + bushes[i + 1]
#     if bush_sum > bush_max:
#         bush_max = bush_sum
#
# print(bush_max)
