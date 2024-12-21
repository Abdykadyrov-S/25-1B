"""
Есть список students 
Выведите каждый элемент из списка отдельно и пронумируйте их 
"""
# students = ['Айданек', 'Бекболот', 'Хасанбай', 'Шахрух', 'Акбар  ', 'Мундуз']

# count = 0
# for student in students:
#     # count = count + 1
#     count += 1
#     print(count, student)

# for i in range(1,7):
#     print(i)


"Цикл while"

"""
while условие:

"""

# if True:
#     print("Hello world!")

# if 5 > 4:
#     print("Hello world!")


# while True:
#     print("Hello world!")

# while 5 > 4:
#     print("Hello world!")

# n = 0
# while n < 5:
#     n += 1
#     print("Hello world!")
# else:
#     print("Конец цикла")


# students = ['Айданек', 'Бекболот',(12345, ), 'Хасанбай', 'Шахрух', 'Акбар  ', 'Мундуз']


# name = 'Айданек'
#       0123456789



# count = 0
# while True:
#     count += 1
#     print(count)


"Модули"

"""
Кастомные модули - lesson.py, main.py, test.py
"""

"""
Встроенные модули - random, datetime, time, math, os
import random 
import os 
"""

# import random
import time

# number = random.randint(1,11)
# print(number)
# time.sleep(1)
# print("Загрузка")
# time.sleep(1)
# students = ['Айданек', 'Бекболот', 'Хасанбай', 'Шахрух', 'Акбар  ', 'Мундуз']

# best_student = random.choice(students)
# print(best_student)

# while True:
#     print("Hello world")
#     time.sleep(2)


"""
Написать игру <Угадай число>
Вы создаете рандомное число с помощью 
# number = random.randint(1,100)
дальше пользователь должен отгадать число
Если он  ввел цифру больше загаданной то выводите надпись
Загаданное число меньше
Точно так же и наоборот
Цикл остановливается если полльзователь угадал число
"""
# import random
# number = random.randint(1,100)

# attempts = 0
# while True:
#     attempts += 1
#     user = int(input("Введите число: "))
#     if user == number:
#         print(f"Вы угадали число {number} за {attempts} попыток")
#         break
#     elif user > number:
#         print("Загаданное число меньше")
#     elif user < number:
#         print("Загаданное число больше")


"Dict - Словари"
"""
dict()
Словарь — неупорядоченная структура данных, 
которая позволяет хранить пары «ключ — значение».
"""

# my_dict = {'name':'Akbar', 'age':17, 'gender': 'M'}
# print(my_dict['age'])
# print(my_dict)
# my_dict_2 = dict(name='Akbar')
# print(my_dict_2)

# my_list = ['Akbar', 17, 'M']
# print(my_list[0])

# my_list = [
#     '1234',
#     12345,
#     23.45,
#     True
# ]

# my_dict = {
#     'name':'Munduz',
#     'age':20,
#     'gender':'M'
# }

# del my_dict['gender']

# print(my_dict)


# my_dict = {
#     'name':'Munduz',
#     'age':20,
#     'gender':'M'
# }
# print(my_dict)
# print(my_dict.keys())
# for i in my_dict:
#     print(i)

# for i in my_dict.keys():
#     print(i)

# print(my_dict.values())
# for i in my_dict.values():
#     print(i)

# print(my_dict.items())

# for k,i in my_dict.items():
#     print(k)
#     print(i)


# my_dict = {
#     'name':'Munduz',
#     'age':20,
#     'gender':'M'
# }

# print(my_dict['hobby'])
# print(my_dict.get('hobby', 'Отсуствует'))
# print(my_dict.get('age', 'Отсуствует'))
# print(my_dict.setdefault('email', 'example@.com'))

# print(my_dict)

# my_dict = {
#     'name':'Munduz',
#     'age':20,
#     'gender':'M'
# }

# my_dict['name'] = 'Adelina'

# print(my_dict)


"Множества в Python (set, frozenset)"

# my_set = {1,2,3,4,5,6,7,8,9}
# my_set = {5,6,1,3,2,4,1,2,6,7,1,9,4,8,7,1}
# my_set = {'a', 'z', 'w', 'w', 'd', 'f', 's', 'c'}

# print(my_set)

# strange_app = set('TikTok')
# strange_app = list('TikTok')
# print(strange_app)

