"""
Создать файл classes09.py.
Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута,
конструктор, геттеры и сеттеры для каждого атрибута, два метода.
"""


class PC:
    def __init__(self, years, type_pc, price):
        self.__years = years
        self.__type_pc = type_pc
        self.__price = price

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, years):
        self.__years = years

    @property
    def type_pc(self):
        return self.__type_pc

    @type_pc.setter
    def type_pc(self, type_pc):
        self.__type_pc = type_pc

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Printers:
    def __init__(self, years, type_printers, color):
        self.__years = years
        self.__type_printers = type_printers
        self.__color = color

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, years):
        self.__years = years

    @property
    def type_printers(self):
        return self.__type_printers

    @type_printers.setter
    def type_printers(self, type_printers):
        self.__type_printers == type_printers

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Disk:
    def __init__(self, type_disk, size, price):
        self.__type_disk = type_disk
        self.__size = size
        self.__price = price

    @property
    def type_disk(self):
        return self.__type_disk

    @type_disk.setter
    def type_disk(self, type_disk):
        self.__type_disk = type_disk

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class CPU:
    def __init__(self, manufacturer, socket, price):
        self.__manufacturer = manufacturer
        self.__socket = socket
        self.__price = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def socket(self):
        return self.__socket

    @socket.setter
    def socket(self, socket):
        self.__socket = socket

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Memory:
    def __init__(self, manufacturer, frequency, type_memory):
        self.__manufacturer = manufacturer
        self.__frequency = frequency
        self.__type_memory = type_memory

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency):
        self.__frequency = frequency

    @property
    def type_memory(self):
        return self.__type_memory

    @type_memory.setter
    def type_memory(self, type_memory):
        self.__type_memory = type_memory


def main():
    pc_1 = PC(2020, 'ноутбук', 2557)
    print(f'Тип ПК: {pc_1.type_pc}, '
          f'год выпуска: {pc_1.years}, '
          f'цена: {pc_1.price} рублей')
    printer_1 = Printers(2019, 'USB', 'черный')
    print(f'Тип принтера: {printer_1.type_printers}, '
          f'год выпуска: {printer_1.years}, '
          f'цвет: {printer_1.color}')
    disk_1 = Disk('SSD', 500, 220)
    print(f'Тип диска: {disk_1.type_disk}, '
          f'объем диска: {disk_1.size}, '
          f'цена: {disk_1.price}')
    cpu_1 = CPU('AMD', 'AM4', 380)
    print(f'Производитель процессора: {cpu_1.manufacturer}, '
          f'сокет: {cpu_1.socket}, '
          f'цена: {cpu_1.price}')
    memory_1 = Memory('Crucial', 3600, 'DDR4')
    print(f'Производитель памяти: {memory_1.manufacturer}, '
          f'частота памяти: {memory_1.frequency}, '
          f'тип памяти: {memory_1.type_memory}')


if __name__ == '__main__':
    main()
