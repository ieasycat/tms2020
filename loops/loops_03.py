"""
Просуммировать неопределенное количество чисел, вводимых пользователем,
суммировать до тех пор, пока пользователь не введёт слово «стоп»
"""

summ = 0
i = 0
while True:
    number = input("Введите число: ")
    if number == 'stop':
        break
    summ += int(number)

print(summ)
print("This's End")
