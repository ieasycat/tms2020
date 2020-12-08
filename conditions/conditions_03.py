"""
Запросить у пользователя возраст.
Если возраст меньше 0 - вывести Wrong input, если меньше 18 - вывести CocaCola, иначе - вывести Beer
"""

old = int(input("Введите Ваш возраст: "))
if old < 0:
    print("Wrong input")
elif old < 18:
    print("CocaCola")
else:
    print("Beer")
