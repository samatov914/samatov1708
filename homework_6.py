# 1) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
# FYI и т.п.

def shorter(phrase):
    phrase_dict = phrase.title().split()
    for i in range(len(phrase_dict)):
        print(phrase_dict[i][0], end='')
shorter('Кыргызская Республика')

# 2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано. Например: “Money, money, money, it’s always sunny, in
# the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
# world: 1

# sam = {}
# def user (ltr):
#     samatov_spl = ltr.lower().split(" ")
#     for name in samatov_spl :
#         sam[name] = samatov_spl.count(name)
# user("Money, money, money, it’s, always, sunny, in, the, richmen’s, world")
# print(sam)


# 3) Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает 

def samat(word):
    izogra1 = list(word)
    izogra2 = set(word)
    if len(izogra1) == len(izogra2):
        return True
    return False
 print(samat("ali"))


# Напишите функцию где мы передаем через аргументы число n как целое
# integer, надо вывести целое число в перевернутом виде
# например: n = 27, тогда перевёрнутое n это 72

def numbers(num):
    return int(str(num)[::-1])
print(numbers(72))


# Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
# духе!” Если вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что”


def sam():
    while True:
        answer = input("спроси что не будь: ")
        if answer.find("?")>=0:
            print("конечно")
        elif answer.find("!")>=0:
            print("успокойся")
        elif answer == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("ну и что")          
sam()