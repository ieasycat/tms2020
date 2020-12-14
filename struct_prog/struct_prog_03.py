"""
Получить на ввод количество рублей и копеек и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки
"""

money_r = int(input("Введите количество рублей: "))
money_k = int(input("Введите количество копеек: "))
x = money_r % 100 < 10 or money_r % 100 > 20
if money_r % 10 == 1 and money_r != 11:
    a = "рубль"
elif money_r % 10 >= 2 and money_r % 10 <= 4 and x:
    a = "рубля"
else:
    a = "рублей"

if money_k % 10 == 1 and money_k != 11:
    b = "копейка"
elif money_k % 10 >= 2 and money_k % 10 <= 4 and x:
    b = "копейки"
else:
    b = "копеек"
print(f'{money_r} {a} {money_k} {b}')
