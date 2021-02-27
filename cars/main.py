"""
Создать ветку cars от master.
Создать пакет cars.
Создать таблицы Brand(name), Car(model,
release_year, brand(foreing key на таблицу Brand)).
Реализовать CRUD(создание, чтение, обновление по id,
удаление по id) для бренда и машины. Создать пользовательский интерфейс.
"""

from cars.ui import functionality_all


def main():
    functionality_all()


if __name__ == '__main__':
    main()
