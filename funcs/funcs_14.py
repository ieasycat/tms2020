"""
Написать 12 функций по переводу:
Дюймы в сантиметры, Сантиметры в дюймы, Мили в километры,
Километры в мили, Фунты в килограммы, Килограммы в фунты,
Унции в граммы, Граммы в унции, Галлон в литры, Литры в галлоны,
Пинты в литры, Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число
Написать программу,
со следующим интерфейсом: пользователю предоставляется на выбор 12
вариантов перевода(описанных в первой задаче).
Пользователь вводит цифру от одного до двенадцати.
После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат.
Использовать функции из первого задания.
Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
"""


def inches_centimeters(number):
    new_number = number * 2.54
    return new_number


def centimeters_inches(number):
    new_number = number / 2.54
    return new_number


def miles_kilometers(number):
    new_number = number / 0.62137
    return new_number


def kilometers_miles(number):
    new_number = number * 0.62137
    return new_number


def pounds_kilograms(number):
    new_number = number / 2.2046
    return new_number


def kilograms_pounds(number):
    new_number = number * 2.2046
    return new_number


def ounces_grams(number):
    new_number = number / 0.035274
    return new_number


def grams_ounces(number):
    new_number = number * 0.035274
    return new_number


def gallon_liters(number):
    new_number = number / 0.26417
    return new_number


def liters_gallon(number):
    new_number = number * 0.26417
    return new_number


def pints_liters(number):
    new_number = number / 1.7598
    return new_number


def liters_pints(number):
    new_number = number * 1.7598
    return new_number


def main():
    print("Аннотация к выбору.")
    print("Выйти из программы - '0'.\nДюймы в сантиметры - '1'. "
          "Сантиметры в дюймы - '2'. Мили в километры - '3'. "
          "Километры в мили - '4'.\nФунты в килограммы - '5'. "
          "Килограммы в фунты - '6'. Унции в граммы - '7'. "
          "Граммы в унции - 8.\nГаллон в литры - '9'. Литры в галлоны - '10'."
          " Пинты в литры - '11'. Литры в пинты - '12'.")

    while True:
        choise = int(input("Выберите: "))
        if choise != 0:
            number = int(input("Введите число: "))
            if choise == 1:
                pr_centimeters = inches_centimeters(number)
                print("Вы выбрали: дюймы в сантиметры.")
                print(f'{number} - {pr_centimeters}')
            elif choise == 2:
                pr_inches = centimeters_inches(number)
                print("Вы выбрали: сантиметры в дюймы.")
                print(f'{number} - {pr_inches}')
            elif choise == 3:
                pr_kilometers = miles_kilometers(number)
                print("Вы выбрали: мили в километры.")
                print(f'{number} - {pr_kilometers}')
            elif choise == 4:
                pr_miles = kilometers_miles(number)
                print("Вы выбрали: километры в мили.")
                print(f'{number} - {pr_miles}')
            elif choise == 5:
                pr_kilograms = pounds_kilograms(number)
                print("Вы выбрали: фунты в килограммы.")
                print(f'{number} - {pr_kilograms}')
            elif choise == 6:
                pr_pounds = kilograms_pounds(number)
                print("Вы выбрали: килограммы в фунты.")
                print(f'{number} - {pr_pounds}')
            elif choise == 7:
                pr_grams = ounces_grams(number)
                print("Вы выбрали: унции в граммы.")
                print(f'{number} - {pr_grams}')
            elif choise == 8:
                pr_ounces = grams_ounces(number)
                print("Вы выбрали: граммы в униции.")
                print(f'{number} - {pr_ounces}')
            elif choise == 9:
                pr_liters = gallon_liters(number)
                print("Вы выбрали: галлон в литры")
                print(f'{number} - {pr_liters}')
            elif choise == 10:
                pr_gallon = liters_gallon(number)
                print("Вы выбрали: литры в галлоны")
                print(f'{number} - {pr_gallon}')
            elif choise == 11:
                pr_liters_g = pints_liters(number)
                print("Вы выбрали: пинты в литры")
                print(f'{number} - {pr_liters_g}')
            elif choise == 12:
                pr_pints = liters_pints(number)
                print("Вы выбрали: литры в пинты(британская)")
                print(f'{number} - {pr_pints}')
        else:
            print("Конец.")
            break


if __name__ == '__main__':
    main()
