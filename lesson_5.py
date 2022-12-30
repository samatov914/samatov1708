#Циклы for, while
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)

# for i in range(1, 1001, 2):
#     print(i)

# names = ["Kurmanbek", "Daniel", "Askhat", "Nursultan"]
# print(type(names))
# for j in names:
#     # print(g)
#     if j == "Askhat":
#         print("Аскат есть")

# numbers = [1, 10, 11, 12, 44, 33, 100, 101, 120, 102, 1111]
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечет")

# name = "Kurmanbek"
# for n in name:
#     if n == "a":
#         print("Буква а есть в имени")
    # print(n)

# number = "100"
# for num in number:
#     print(num)

# cities_tup = ("Osh", "Bishkek", "Talas", "Tokmok")
# for city in cities_tup:
#     print(city)

# cars = {"BMW", "MERSEDES", "TESLA", "HONDA"}
# for i in cars:
#     print(i)

# student = {"name" : "Daniel", "age" : 18, "language" : "Python"}
# for key, value in student.items():
#     # print(key, value)
#     if key == "language" and value == "Python":
#         print("Питонист найден")
#     else:
#         print("Else")

# numbers = []
# for n in range(1, 101):
#     numbers.append(n)
# print(numbers)

# for i in range(1, 11):
#     print(i)
#     if i == 6:
#         print("STOP")
#         continue

# numbers = [10, 20, 30, 40, 50, "Hello"]
# for i, n in enumerate(numbers):
#     print(i, n)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     print(num1)
#     # num1 = num1 + 1
#     num1 += 1

# import random

# n = 0
# random_number = random.randint(1, 10000)
# print(random_number)
# while True:
#     n += 1
#     print(n)
#     if n == random_number:
#         print("Найден")
#         break

import time

process = 0
while True:
    print(str(process) + "% HACK")
    process += 5
    time.sleep(0.5)
    if process == 100:
        print("HACKED")
        break