"""
Ввести число, проверить на то, что было введено именно число. Возвести его в куб.
"""

number = input("Введите число: ")
if number.isdigit():
    print(int(number) ** 3)
else:
    print("Введите число!")
