"""
Пользователь вводит время в минутах и расстояние в километрах.
Нужно найти скорость в м/с
"""

time = int(input("Введите время в минутах: "))
distance = int(input("Введите расстояние в километрах:"))

time_s = time * 60
distance_m = distance * 1000

speed = int(distance_m / time_s)

print(speed, "м/с")
