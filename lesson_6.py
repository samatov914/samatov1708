# fun

# def cals():
    # num1 = int(input("Введите первое число:"))
    # num2 = int(input("Введите второе число:"))
#     print(num1 + num2)
# cals()

# def cals(num1, num2):  #Параметры num1, num2
#     print(num1 + num2)
# cals(10, 20)     # К параметрам num1, num2 передаются аргументы 10 и 20

# def hello_world():
#     print("Hello World")
# # hello_world()


# def func_while():
#     while True:
#         print("GeekTech")
# func_while()


# numbers = [10,20,1,4,5,2,44]
# print(max(numbers))

# def max(arg):
#     print("GeekTech")
# print(max(numbers))

# def print(word):
#     pass
# print("Hello Word")

# def hello_user(name : str) -> str:
#     print("Здраствуйте", name)
# hello_user("Askhat")
# hello_user("Asylbek")
# hello_user("Daniel")
# hello_user(30)

# def add(num1 : int, num2 : int):
#     print(num1 + num2)

    
# def sub(num1 : int, num2 : int):
#     print(num1 - num2)

    
# def mult(num1 : int, num2 : int):
#     print(num1 * num2)

    
# def div(num1 : int, num2 : int):
#     print(num1 / num2)


# def main(num1 : int, num2 : int, operator : str):
#     if operator == "+":
#         add(num1, num2)
#     elif operator == "-":
#         sub(num1,num2)
#     elif operator == "*":
#         mult(num1,num2)
#     elif operator == "/":
#         div(num1,num2)
#     else:
#         print("Error")
# main(30,30, "/")
# main(30,150, "*")
# main(30,25, "-")
# main(1,9999999999, "+")


# def chet_nechet(number : int = 2) -> :
#     if number % 2 == 0:
#         print(number,"Четный") 
#     else:
#         print(number,"Нечетный")
# chet_nechet(222)
# chet_nechet(333)
# chet_nechet(3)

# numbers = [10,22,33,42,44,55,1,2,3,4,5,101,111,112]
# tup_numbers = (2,3,4,5,32,52,53,34)
# def list_chet(lst_num : list) -> str:
#     for num in lst_num:
#         if num % 2 == 0:
#             print(num, "Четный")
#         else:
#             print(num, "нечетный")
# list_chet(numbers)
# list_chet(tup_numbers)

def hello():
    return "Hello GeekTech"
print(hello())