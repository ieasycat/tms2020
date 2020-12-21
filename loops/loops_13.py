"""
Создать список с фамилиями.
Вывести все фамилии, которые начинаются на П и заканчиваются на а
"""


def print_new(last_name):
    last_name_new = []
    for name in last_name:
        if name[0] == 'П' and name[-1] == 'а':
            last_name_new.append(name)
    print(", ".join(last_name_new))


def main():
    last_name_list = ["Клименко", "Петров", "Плотва",
                      "Петровна", "Ломако", "Пахлона"]
    print_new(last_name_list)


if __name__ == '__main__':
    main()
