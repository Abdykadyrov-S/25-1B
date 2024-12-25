"Встроенные функции"
# input
# len
# max
# int

"Функции"

"""
def назв_функ():
    тело функции
    изоллированный код

назв_функ()
"""

# def name_func():
#     print("Hello world!")

# name_func()

# input()

# if 5 > 6:
#     name_func() 
# else:
#     name_func() 



# import random

# def game():
#     number = random.randint(1,100)

#     attempts = 0
#     while True:
#         attempts += 1
#         user = int(input("Введите число: "))
#         if user == number:
#             print(f"Вы угадали число {number} за {attempts} попыток")
#             print("Вы хотите начать заново + да, - нет: ")
#             user_choice = input(": ")
#             if user_choice == '+':
#                 game()
#             elif user_choice == '-':
#                 break
#             else:
#                 print("Введите '+' да и '-' нет")
#         elif user > number:
#             print("Загаданное число меньше")
#         elif user < number:
#             print("Загаданное число больше")

# game()

# def add():
#     num = int(input("ВВедите первое число: "))
#     num2 = int(input("ВВедите второе число: "))

#     print(f"{num} + {num2} = {num + num2}") 

# add()


"""
def назв_функ(аргументы):
    тело функции
    изоллированный код

назв_функ()
"""

# def add(a,b):
#     print(a + b)

# add(2,3)

# def main(text):
#     for i in text:
#         print(i)
#     print(text)

# main(['12',1,2,4,67])


# def add(a: int, b: int) -> int:
#     print(a + b)

# add(5, 5)


# def add(a: int, b: int) -> int:
#     # print(a + b)
#     return a + b

# # add(5, 5)

# text = "qwertyu"
# res = len(text)
# print(res)

# res_add = add(2,3)
# print(res_add)



# def main():
#     print("Hello world!")
#     return "Hello world!"

# main()


# def register(name, age, gender):
#     print(f"имя-{name}, возраст-{age}, пол-{gender}")

# register(age=16, gender="M", name="Hasan")

"""
*args - *
**kwargs - **
неопределенное количество позиционных или именованных аргументов
"""

# def register(name, age, gender):
#     print(f"имя-{name}, возраст-{age}, пол-{gender}")

# register(*["Abdulloh", 16, "M"]) 

# def register(name, age, gender, *other_data):
#     print(f"имя-{name}, возраст-{age}, пол-{gender}")
#     for i in other_data:
#         print(i)
#     print(other_data)

# register("Abdulloh", 16, "M", 12, 23, 'email', 'hobby') 



def register(name, age, gender, **other_data):
    print(f"имя-{name}, возраст-{age}, пол-{gender}")
    for i in other_data:
        print(i)
    print(other_data)

register("Abdulloh", 16, "M", hobby="football", email="gmail.com")
