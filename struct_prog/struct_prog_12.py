"""
Дан список целых чисел.
Подсчитать сколько четных чисел в списке
"""

listt = [2, 4, 5, 8, 13, 18, 42, 99]
listt_new = []
i = 0
while i < len(listt):
    if listt[i] % 2 == 0:
        listt_new.append(listt[i])
    i += 1
print(len(listt_new))
