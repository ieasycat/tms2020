"""
Дан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.
"""

list_number = [15, 3, 7, 11, 34]
i = 0
summ = 0
while i < len(list_number):
    if list_number[i] > 10:
        summ += list_number[i]
    i += 1
print(summ)
print("This's End")
