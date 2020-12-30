# for, while

# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1  # i = i+1

# num = int(input("Enter number: "))
# i = 1
# total = 0
#
# while i <= num:
#     value = int(input("Enter value: "))
#     total = total + value
#     i += 1
#
# print(f"Total number is : {total}")

# i = 1
# while i < 10:
#     i += 1
#     if i == 5 or i == 7:
#         # print("I am five")
#         continue
#         # break
#
#     print(i)


# data = ['Ram', 'Sita', 'Gita']  # list
# print(data[1])
# for user in data:
#     print(user)

# data = [
#     ["Ram", "Sita", "Gita"],
#     ["Hari", "Madan", "Kabita"],
#     ["Sophia", "Kalpana", "Nandira"]
# ]
#
# for users in data:
#     for user in users:
#         print(user)


# num = int(input("Enter number of users: "))
# i = 1
# users = []  # Empty list
#
# while i <= num:
#     name = input("Enter name: ")
#     users.append(name)
#     i += 1
#
# for user in users:
#     print(user)


# i = 0
# even = 0
# odd = 0
# while i <= 10:
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
#     i += 1
#
# print(f"Even total: {even}")
# print(f"Odd total: {odd}")

for a in range(0, 10):
    print(a)
