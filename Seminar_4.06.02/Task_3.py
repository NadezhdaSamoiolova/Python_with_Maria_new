# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

# n = int(input())
# max_number = 0
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

n = int(input())
max_number = -1
while n > 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)
