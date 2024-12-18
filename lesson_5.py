"List - Списки" 

# my_list = [1, (12,12), "q"]
# my_str = '1, (12,12), "q"'

# # my_list[0] = "qwer" 
# print(type(my_list))

# my_tuple = (True,)

# print(type(my_tuple))


"Циклы - for, while"

"""Циклы предназначены для повторения определенного 
кода и для перебора значений в итерируемых типах данных"""

"""
for переменное in итерируемый Т.П:
    тело цикла

for переменное in range(5):
    тело цикла

"""
# sp_nu = [0, 1,2,3,4,5,6,7,8, ...]
# range(0, 5) 


# 0,1,2,3,4
# for number in range(5):
#     print(number)
#     print("Hello world") 


my_list = [1, (12,12), "q", 12, 5.6]
#          0     1      2   3    4

# print(type(my_list[0]))
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

# for i in my_list:
#     print(i)


# students = ['Айданек', 'Бекболот', 'Хасанбай']

# for student in students:
#     # # 1
#     # student = 'Айданек'
#     # print("Привет" , students[0])
#     # # 2
#     # student = 'Бекболот'
#     # print("Привет" , students[1])
#     # # 3
#     # student = 'Хасанбай'
#     # print("Привет" , students[2])
#     # ---------------------------
#     print("Привет" , student)
#     print("Привет")




# print("Привет" , students[0])

"""
break, continue 
"""


# name = "Geeks"
# password = "2021"
# for i in range(3):
#     user_name = input("Введите логин: ")

#     if name == user_name: 
#         user_passw = input("Введите пароль: ")
#         if password == user_passw:
#             print("Добро пожаловать!")
#             break 
#         else:
#             print("Пароль не верный")
#     else:
#         print("Пользователь с таким login отсутвует")


# for i in range(5):
#     print('Hello world #1')
#     # print('Hello world #2')


# students = ['Айданек', 'Бекболот', 'Хасанбай', 'Шахрух', 'Акбар	', 'Мундуз']


# for student in students[:3]:
#     print(student)

# for student in students:
#     if student == 'Хасанбай':
#         continue 
#     print(student)


# for i in range(20, 49, 2):
#     print(f"{i}) Hello world")

"""
Есть список students 
Выведите каждый элемент из списка отдельно и пронумируйте их 
"""
students = ['Айданек', 'Бекболот', 'Хасанбай', 'Шахрух', 'Акбар  ', 'Мундуз']


