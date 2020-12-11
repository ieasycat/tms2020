"""
Получить на ввод количество рублей и копеек и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки
"""

money_r = int(input("Введите количество рублей: "))
money_k = int(input("Введите количество копеек: "))
x = money_r % 100 < 10 or money_r % 100 > 20
if money_r % 10 == 1 and money_r != 11:
    if money_k % 10 == 1 and money_k != 11:
        print(f"{money_r} рубль {money_k} копейка")
elif money_r % 10 >= 2 and money_r % 10 <= 4 and x:
    if money_k % 10 >= 2 and money_k % 10 <= 4 and x:
        print(f"{money_r} рубля {money_k} копейки")
else:
    print(f"{money_r} рублей {money_k} копеек")
