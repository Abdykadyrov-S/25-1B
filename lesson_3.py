
"""
STRING - str - последоваиельность символов (текст)
str()
"""

# num1 = 123
# num2 = '123'

# text = "Индексы - Нумерация элементов"

# letters = 'abdcefg'
# #          0123456

# print(letters[3])

' '
# 
" "
# 
""" """
# 
''' '''

# letters = 'abd cefg'
# #          01234567
# print(letters[3])

"Форматирование строк"
".format()"

# num1 = int(input(": "))
# num2 = int(input(": "))

# print("Результат сложения:", num1, "+", num2, "=", num1 + num2)
# print(f"Результат сложения: {num1} + {num2} = {num1 + num2}")
# res = f"Результат сложения: {num1} + {num2} = {num1 + num2}"

"Конкантенация - это склеивание строк через оператор  +"

# num1 = input(": ")
# num2 = input(": ")

# print(f"Результат сложения: {num1} + {num2} = {num1 + num2}")

# name = input("Введите имя: ")

# res = "Привет" + " " + name

# print(res)


"""
Создайте две переменные 
1 - для названия книги
2 - для года выпуска данной книги
Ввыведите в терминал красиво данные с использованием <f> строки
Так же объедините две переменные в одну переменную 
и выведите в терминал 
"""

"Индексы и срезы"

letters = 'abdc efg qwertyuiop'
#          01234567
#                      -4-3-2-1
"""
[2] - выводит элемент с таким индексом
[начало:конец:шаг]
[:]
[:6]
[0:4]
"""
# print(letters[2:6])
# print(letters[:4])
# print(letters[5:11])
# print(letters[5:])
# print(letters[::2])
# print(letters[::3])
# print(letters[-2])

"Условия. Условные операторы"
"""
if - условный оператор который создает конструкцию 
if условие:
    что должно произойти если условие правильное
    тело условного оператора if
    код который должен сработать
if True:
    действие сработает
if False:
    действие не сработает

elif - у.оп который дополняет условие (if) (пишется неограниченно)

else - иначе (в иноч случае)
"""

# if 6 > 4:
#     print("Hello world")

# if False:
#     print("Hello world")

# print(6 > 4)

# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))

# if number1 > number2:
#     print(f"{number1} больше чем {number2}")
# elif number1 > number2:
#     print(f"{number1} больше чем {number2}")
# elif number1 < number2:
#     print(f"{number1} меньше чем {number2}")
# else:
#     print("Они равны")


# name = "Geeks"
# password = "2021"

# user_name = input("Введите логин: ")
# user_passw = input("Введите пароль: ")

"Не верно"
# if name == user_name:
#     print("Добро пожаловать!")
# elif password == user_passw:
#     print("Добро пожаловать!")

"Верно (вложенная конструкция)"
# if name == user_name:
#     if password == user_passw:
#         print("Добро пожаловать!")
# else:
#     print("Неверный логин или пароль")

"Операторы and, or"

# if name == user_name and password == user_passw:
#     print("Добро пожаловать!")
# else:
#     print("Неверный логин или пароль")

# if name == user_name or password == user_passw:
#     print("Добро пожаловать!")
# else:
#     print("Неверный логин или пароль")


"Верно (вложенная конструкция)"
name = "Geeks"
password = "2021"

user_name = input("Введите логин: ")

if name == user_name:
    user_passw = input("Введите пароль: ")
    if password == user_passw:
        print("Добро пожаловать!")
    else:
        print("Пароль не верный")
else:
    print("Пользователь с таким login отсутвует")
    