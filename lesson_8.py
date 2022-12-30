# # # def div(num1 : int = 2, num2 : int = 2)-> float:
# # #     try:
# # #         return num1/num2
# # #     except ZeroDivisionError:
# # #         return"Деление на ноль. Учи математику"
# # #     except TypeError:
# # #         return"Пиши целые числа"
# # # print(div(10,5))
# # # print(div(10,2))
# # # print(div(10,0))
# # # print(div("10","0"))

# # def calc():
# #     while True:
# #         try:
# #             num1 = int(input("Введите первое число: "))
# #             operator = input ("+, -, *, / :")
# #             num2 = int(input("Введите второе число: "))
            
# #             if operator == "+":
# #                 print(num1 + num2)
# #             elif operator == "-":
# #                 print(num1-num2)
# #             elif operator == "*":
# #                 print(num1*num2)
# #             elif operator == "/":
# #                 try:
# #                     print(num1/num2)
# #                 except ZeroDivisionError:
# #                     print("Деление на ноль")
# #             else:
# #                 print("Оператор не найден")
# #         except ValueError:
# #             print("Ввод целыми числами")           
# # calc()

# # try:
# #     print(10/0)
# # except:
# #     print("Error")
# #     raise ValueError("Специально вывели ошибку с помощью raise")
# # finally:
# #     print("Я всегда буду работать ")

# # f = open('hello.txt', 'w')
# # f.write("GeekTech")
# # f.close()

# # r = open('Hello.txt', 'r')
# # print(r.read())
# # r.close

# # import time
# # print(time.ctime())

# # def save_login_password(login:str, password:str)-> str:
# #     password_file = open('login_passwords.txt','a+')
# #     if login and len(password)>=8 and ' ' not in password:
# #         password_file.write(f"{login}, {password}{time.ctime()}\n")
# #     else:
# #         return"Неправильный логин и пароль"
# #     password_file.close()
# #     return "Логин и пароль сохранен"

# # print(save_login_password('geektech', 'geektech2023'))
# # print(save_login_password('Askhat', 'GeekCoin'))
# # print(save_login_password('Nurbolot', 'GeekCoin_2'))
# # # print(save_login_password('anonimus', '     '))

# # with open('geek.txt', 'a+') as g:
# #     g.write("Askhat\n")

# # with open('geek.txt', 'r')as r:
# #     print(r.read())


# import random
# # print(random.randint(1,10))

# def generate_random_number():
#     return random.randint(1,10)
    
# def user_contact(name:str, number:str, secret_key:str):
#     with open('wins.txt,' 'a+' encoding = 'utf-8' )as win:
#         win.write(f"Имя: {name}, Номер: {number}, Ключ: {secret_key}, дата: {time.ctime}\n")


# def main():
#     random_number = generate_random_number()
#     n = 0 
#     while True:
#         user_input = int(input("Введите число: "))
#         n += 1
#         if random_number == user_input:
#             print("Вы выиграли! Введите свои данные для контакта")
#             # name = input("Введите свое имя: ")
#             number = input("Введите свой номер :")
#             secret_key = input("Введите секретное слово для получение приза:")
#             user_contact(name,number,secret_key)
#             print("Спасибо, ваши данные записаны")

#         else:
#             print(f"Вы не угадали{5 - n} попыток ")
#             if 5 - n == 0:
#                 break

# main()

print("GeekStudio")