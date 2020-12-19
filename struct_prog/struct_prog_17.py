"""
Дано число. Найти сумму и произведение его цифр.
"""


my_number = int(input("A: "))

my_summ = 0
my_mult = 1

while my_number > 0:
    my_remains = my_number % 10
    if my_remains != 0:
        my_summ += my_remains
        my_mult *= my_remains
    my_number = my_number // 10

print("Сумма:", my_summ)
print("Произведение:", my_mult)
