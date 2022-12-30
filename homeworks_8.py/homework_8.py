# 1 Напишите функцию, которая принимает список, из списка выдает случайное
# значение из списка и записывает результат в txt файл. Список language =
# ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]

# import random 
# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# def sam(sams):
#     samatov = random.choice(sams)
#     with open('samatov.txt', 'a+') as f:
#         f.write(f"{samatov}\n")
# sam(language)


# 2 У нас есть переменная text которая, хранит в себе текст:
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# Откройте файл text.txt и запишите текст в файл 2 способами


# f = open('makambaev.txt', 'w' )
# f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.') 
# f.close()


# with open('asdf.txt', 'a+') as f:
#     f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

# # 3) Написать программу, которая откроет созданный в задаче 2 файл text.txt,
# скопирует весь текст и запишет его в новый файл wikipedia.txt .

with open('makambaev.txt','r')as f,open('asdf.txt', 'r')as v,open('wikipedia.txt','a')as k:
    for i in f:
        k.write(i)
    for s in v:
        k.write(s)