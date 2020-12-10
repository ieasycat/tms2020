"""
Выведите на экран n раз фразу "Silence is golden". Число n вводит пользователь.
"""

quantity = int(input("Введите количество повторов: "))
while quantity != 0:
    print("Silence is golden")
    quantity -= 1
print("This's End")
