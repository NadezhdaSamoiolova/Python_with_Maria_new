# * 4. Требуется определить, можно ли
# от шоколадки размером n × m долек
# отломить k долек, если
# разрешается сделать один разлом
# по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# in
# 3 2 4
#
# out
#
# yes
#
# in
# 3 2 1
#
# out
#
# no

m = int(input())
n = int(input())
k = int(input())
if (k % m == 0 or k % n == 0) and k < m * n:
    print("Yes")
else:
    print("No")
