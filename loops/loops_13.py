"""
Создать список с фамилиями.
Вывести все фамилии, которые начинаются на П и заканчиваются на а
"""

last_name = ["Клименко", "Петров", "Плотва", "Петровна", "Ломако", "Пахлона"]
last_name_new = []
for name in last_name:
    if name[0] == 'П':
        if name[-1] == 'а':
            last_name_new.append(name)
print(", ".join(last_name_new))
