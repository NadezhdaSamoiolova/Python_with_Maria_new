# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


# A = int(input("Input number A: "))
# B = int(input("Input number B: "))


#
# print("Your result is: ", int(A ** B))
def grade(A, B):
    if B == 1:
        return A
    else:
        num = B - 1
        return A * grade(A, num)


print(grade(3, 1))

##### Solution of Maria

# def pow_num(a, b):
#     if b == 0:
#         return 1
#     if b < 0:
#         return pow_num(a, b + 1) * 1 / a
#     return pow_num(a, b - 1) * a
