"""
Дан список целых чисел.
Подсчитать сколько четных чисел в списке
"""

listt = [2, 4, 5, 8, 13, 18, 42, 99, 66]
i = 0
count = 0
while i < len(listt):
    if listt[i] % 2 == 0:
        count += 1
    i += 1
print(count)
