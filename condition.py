# username = "admin"
# password = "admin002"
# if username == "admin" and password == 'admin002':
#     print("Welcome" + username)
# else:
#     print("Username & password not match")

# x = 10
# y = 20
# z = 30
# if x > y and x > z:
#     print("x")
# elif y > x and y > z:
#     print("y")
# else:
#     print("z")

# if x > y:
#     print("X is large")
# else:
#     print("Y is large")

# a = 12
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# nep = int(input("Enter number"))
# nep = input("Enter number")
# nep = int(nep)
# print(type(nep))

"""
nep,eng,mat,sic,pop
find out: total,percentage,divison - f,s,t
if pre = 40 to 60 s, 60 -75 f;

"""
#
# x = 10
# y = 20
# z = 30
#
# if x > y:
#     if x > z:
#         print("x")
#     else:
#         print("z")
# else:
#     if y > z:
#         print("Y")
#     else:
#         print("z")
# string
nep = int(input("Nepali: "))
eng = int(input("English: "))
mat = int(input("Math: "))
sic = int(input("Science: "))
pop = int(input("Population: "))
total = nep + eng + mat + sic + pop
pre = total / 5

if pre < 40:
    pass
