# Ввести число с клавиатуры.
# Вернуть результат логического выражения: число больше 15 и число кратно (%) 5.

x = int(input('Введите  любое число: '))
a = x > 15 and x % 5 == 0
print(a)
