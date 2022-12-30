#  Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужно
# превратить кортеж в список и добавить новое значение ‘Tesla’, затем
# превращаете список обратно в кортеж

it_company = ("Google", "Amazon", "Microsoft")
print(it_company)
lst_cars = list(it_company)
print(lst_cars)
lst_cars.append("Tesla")
print(lst_cars)
cars = tuple(lst_cars)
print(cars)


lst_company = list(it_company)
print(it_company)
lst_company.append("Tesla")
print(lst_company)
it_company = tuple(lst_company)
print(lst_company)
# 2) Из 1 задания попробуйте вывести индекс ‘Amazon'
# print(it_company.index("Amazon"))


# # 3) Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способами
# it_company = ("Google", "Amazon", "Microsoft")
# tup = tuple(it_company)
# print(tup)
# lst = list(tup)
# print(lst)
# lst[0] = "Apple"
# tup = tuple(lst)
# print(tup)

# # 5

text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
'with', 'our', 'python', '3', 'overview')
print(text_tuple.count("python"))

# # 6

# Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd':
# 600}. Объедините их в один при помощи встроенных функций языка Python.
# Подсказка: метод update()

# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd':600}
# dictionary_1.update (dictionary_2)
# print(dictionary_1)


# 7 Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2,
# ‘num_3’ : 3, ‘num_100’ : 100} Необходимо умножить все числовые значения
# словаря на 5 и вывести в терминал.

numbers = {"num_1" : 1, "num_2" : 2,
"num_3" : 3, "num_100" : 100}

numbers["num_1","num_2", "num_3", "num_100"  ] = 1 * 2,2 * 2,3 * 2,100 *2
print(numbers)
# 8

# Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза

# student = {"name" : "Askhat", "age" : 17}
# student["age"] = 17 * 2
# print(student)


# 9) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}. Обновите age в 16

# student = {"name" : "Askhat", "age" : 17, "color" : "White"}
# student["age"] = 17 - 1
# print(student)

# 10) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Удалите ключ и значение age

# student = {"name" : "Askhat", "age" : 17}
# student.pop("age")
# print(student)

# 11) Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и значение(Западный Анар)

# student = {"name" : "Askhat"}
# student.setdefault('address', 'Западный Анар') #Добавляем с словарь новый ключ и значение
# print(student)

# 12) Напишите программу, которая имитирует проверку пароля, придуманного
# пользователем. Пользователь вводит пароль, а потом ещё раз его же, для
# подтверждения. И пароль который вводит пользователь записывается в пустое
# множество после проверок
# Если первый пароль, который ввел пользователь короче 8 символов, программа
# выводит на экран слово "Короткий пароль!"
# Если же первый пароль достаточно длинный, но в нём содержится сочетание
# символов "123", программа выводит на экран слово "Простой пароль!"
# Если же предыдущие проверки пройдены успешно, но введённые слова-пароли не совпадают, то программа выводит на экран слово "Различаются." Если же и третья проверка пройдена успешно, программа выводит "OK" (латинскими буквами) и выводит “Пароль создан!”

# contacts = ["Askhat"]
# while True:
#     sam = input("Введите пароль: ")
#     num1 = sam.find("123")
#     if len(sam)>7:
#         if num1 < 0:
#             password.setdefault("first_p",sam)
#             proverkra_password = input("Введите повторный пароль:")
#             if password[first]
print (1.500 + 1.500)
num = float(2)
x = 12
y = 11
print(y + 12 + x)
print(int(1.99999))
print([1,2] == [2,1])