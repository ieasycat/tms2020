"""
Дан словарь: {'test': 'test_value', 'europe': 'eur',
 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)
Предоставить 2 решения. Одно с использованием цикла while,
другое с использованием цикла for с параметром.
Оба решения предоставить в одном файле.
"""


def my_for(x):
    for key in list(x.keys()):
        new_key = key + str(len(key))
        x[new_key] = x.pop(key)
    return x


def my_while(x):
    keys = list(x.keys())
    i = 0
    while i < len(keys):
        new_keys = keys[i] + str(len(keys[i]))
        x[new_keys] = x.pop(keys[i])
        i += 1
    return x


def main():
    my_dictt = {'test': 'test_value', 'europe': 'eur',
                'dollar': 'usd', 'ruble': 'rub'}
    for_one = my_for(my_dictt)
    my_dictt = {'test': 'test_value', 'europe': 'eur',
                'dollar': 'usd', 'ruble': 'rub'}
    while_two = my_while(my_dictt)
    print(f"This's Loops(for) - {for_one}")
    print(f"this's Loops(while) - {while_two}")


if __name__ == '__main__':
    main()
