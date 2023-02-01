# Найдите сумму цифр трехзначного числа.
# in
# 123

# out
# 6

# in
# 100

# out
# 1

a = int(input("Input your 3-digits number: "))
res = 0
while a > 0:
    b = a % 10
    a = a // 10
    res += b
print(res)
