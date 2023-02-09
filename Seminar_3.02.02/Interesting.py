### Comprehension ###

# num = []
# for i in range(0, 26, 2):
#     num.append(i)
#
# print(num)


# num = []
# num = [i for i in range(0, 26, 2)]
# print(num)


# num = []
# num = [i for i in range(26) if i % 2 == 0]
# print(num)


# num = []
# num = [i+10 for i in range(26) if i % 2 == 0]
# print(num)


# num = []
# num = [i+10  if i % 2 == 0 else i ** 3 for i in range(26)]
# print(num)


# num = {i: i ** 3 for i in range(26)}
# print(num)
#

# num = {i: i ** 3 for i in range(1, 11)}
# print(num)


# num = {k: v ** 3 for k in "ALJLFHBL" for v in range(1, 11)}
# print(num)

# num = {}
# for k in "ALJLFHBL":
#     for v in range(1, 11):
#         num[k] = v ** 3
# print(num)

num = {k: v ** 3 for k, v in zip("ASDFGHJK", range(1, 11))}
print(num)
