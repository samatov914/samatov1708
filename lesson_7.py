# Лямбда Функции
# def hello_world(x):
#     return x * x
# print(hello_world(10))

# hello = lambda x: x * x
# print(hello(10))

# print((lambda x: x * x)(10))


#################################################3


# def mult(num1 : int = 2, num2 : int = 2)-> int:
#     return num1 * num2
# print(mult(10,5))
# print(mult())

# lambda_mult = lambda num1, num2: num1 * num2
# print(lambda_mult(10,5))

# print(lambda num1, num2: num1 * num2(10,5))


# number = [10,50,30,25,2,12,45,36,55,21,23]
# chet = []

# def chet_func(num : list) -> list:
#     for i in num:
#         if i % 2 == 0:
#             chet.append(i)
#     return chet
# print (chet_func(number))

# ######number = [10,50,30,25,2,12,45,36,55,21,23]##########################################
# number = [10,50,30,25,2,12,45,36,55,21,23]
# chet = list(filter(lambda num: num % 2 == 0, number))
# print(chet)

# ####################################################
# number = [10,50,30,25,2,12,45,36,55,21,23]
# print(list(filter(lambda num: num % 2 == 0, number)))


# ##############################################################333


# print(list(filter(lambda num: num % 2 == 0,[10,50,30,25,2,12,45,36,55,21,23])))


# num = [10,20,30,40,50]
# lst = []
# def mult_two(num_list : list) -> list:
#     for i in num_list:
#         lst.append(i * 2)
#     return lst
# print(mult_two(num))

# ###########################################################################
# num = [10,20,30,40,50]
# lst = list(map(lambda num_list: num_list * 2, num))
# print(lst)

# ###################################################

# num = [10,20,30,40,50]
# print(list(map(lambda num_list: num_list * 2, num)))

# #####################################################

# print(list(map(lambda num_list: num_list * 2, [10,20,30,40,50])))

######################МОДУЛИ#######################################

# import time 

# def get_time():
#     return time.ctime()

# def hello():
#     return "Hello World"

# it = "GeekTech"
# print(hello())
# print(get_time())

numbers = [1,2,3,4,5,6,7,8,9,10]
chet = []
