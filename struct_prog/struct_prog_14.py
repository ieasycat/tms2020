"""
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 ->  2 3 4 5 1
предоставить 2 решения. Одно с использованием цикла while,
другое с использованием цикла for с параметром.
Оба решения предоставить в одном файле.
"""


def my_for(x):
    listt_two = []
    for i in x:
        listt_two.insert(len(listt_two) - 1, i)
    return listt_two


def my_while(x):
    listt_two = []
    i = 0
    while i < len(x):
        listt_two.insert(len(listt_two) - 1, x[i])
        i += 1
    return listt_two


def main():
    listt_one = [1, 9, 3, 4, 5, 2, 13]
    print_for = my_for(listt_one)
    print_while = my_while(listt_one)
    print(f"This's Loops(for) - {print_for}")
    print(f"This's Loops(while) - {print_while}")


if __name__ == '__main__':
    main()
