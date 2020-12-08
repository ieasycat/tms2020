"""
Ввести 3 числа. Первое увеличить в 2 раза, второе уменьшить на 3, третье число возвести в квадрат.
После найти сумму трех чисел
"""

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))

result_number_1 = number_1 * 2
result_number_2 = number_2 - 3
result_number_3 = number_3 ** 2

summ = result_number_1 + result_number_2 + result_number_3
print(result_number_1, "+", result_number_2, "+", result_number_3, "=", summ)

