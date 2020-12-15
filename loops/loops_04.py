"""
Просуммировать неопределенное количество чисел,
вводимых пользователем, суммировать до тех пор,
пока пользователь не введёт слово «стоп».
Не учитывать числа кратные 5
"""

summ = 0
i = 0
while True:
    number = input("Введите число: ")
    if number == 'stop':
        break
    elif int(number) % 5 == 0:
        continue
    summ += int(number)

print(summ)
print("This's End")
