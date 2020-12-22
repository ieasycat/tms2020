"""
Написать программу,
в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак операции,
а также на ввод Y=0 при делении.
Организовать возможность многократных вычислений без перезагрузки программа
(т.е. построить бесконечный цикл).
В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
"""


def main():
    while True:
        summ = 0
        print("0 в качестве операции служит для завершение работы")
        operators = input("Введите какую операцию Вы хотите совершить: ")
        if operators == '0':
            break
        if operators in ('+', '*', '/', '-'):
            one_number = int(input("Введите 1-ое число: "))
            two_number = int(input("Введите 2-ое число: "))
            if operators == '+':
                summ = one_number + two_number
            elif operators == '-':
                summ = one_number - two_number
            elif operators == '*':
                summ = one_number * two_number
            elif operators == '/':
                if two_number != 0:
                    summ = one_number / two_number
                else:
                    print("Нельзя делить на 0")
                    continue
        else:
            print("Вы ввели неверный знак операции.")
        print(f'{summ}')
    print("Конец.")


if __name__ == '__main__':
    main()
