# Запрашиваем 2 целых числа
# Выводим сумму числе в виде a + b = c
# Перед тем, как почситать, преоброжомаем строку в int

number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
summ = number_one + number_two
print(f'{number_one} + {number_two} = {summ}')