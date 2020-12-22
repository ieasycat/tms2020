"""
Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
"""


def my_enumeration(a, b):
    for i in range(a, b):
        one = 0
        two = 0
        for x in range(1, i):
            if i % x == 0:
                one += x
        for j in range(1, one):
            if one % j == 0:
                two += j
        if i == two and i != one and i == min(i, one):
            print(i, one)


def main():
    number_one = 200
    number_two = 300
    my_enumeration(number_one, number_two)


if __name__ == '__main__':
    main()
