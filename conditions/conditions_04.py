"""
Ввести строку с клавиатуры
Если длина строки больше 5 - вывести значение на экран
Если длина строки меньше 5 - вывести строку “Need more!”
Если длина строки равна 5 - вывести строку “It is five”
"""

text = input("Введите строку: ")
x = len(text)
if x > 5:
    print(text)
elif x < 5:
    print("Need more!")
else:
    print("It is five")