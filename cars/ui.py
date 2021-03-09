from cars.buisness_logic import create_car, create_brand, \
    read_car, read_brand, update_car, update_brand, delete_car, delete_brand, \
    WrongChoice, IdError, WrongName
from cars.car import Car, Brand, session


def display_car():
    cars = read_car()
    if cars:
        for car in cars:
            print(car)
    else:
        print('\nМашин нет.')
    print()


def display_brand():
    brands = read_brand()
    if brands:
        for brand in brands:
            print(brand)
    else:
        print('Брендов нет.')
    print()


def add_car():
    check, model = check_car()

    if not check:
        release_year = int(input('Введите год машины: '))
        print()
        display_brand()
        my_id = int(input('Выберите ID бренда: '))
        brand = session.query(Brand).filter_by(id=my_id).first()
        create_car({'model': model,
                    'release_year': release_year,
                    'brand': brand},
                   )
    else:
        raise WrongName
    print()


def check_car():
    model = input('Введите модель машины: ')
    check = session.query(Car.model).filter_by(model=model).first()
    return check, model


def check_brand():
    name = input('Введите название бренда: ')
    check = session.query(Brand).filter_by(name=name).first()
    return check, name


def add_brand():
    check, name = check_brand()

    if not check:
        create_brand({'name': name})
    else:
        raise WrongName
    print()


def change_car():
    print('Введите "0" для выхода в предыдущее меню.')
    car_id = int(input('Выберите ID машины, которую хотите изменить: '))

    check_id = session.query(Car).filter_by(id=car_id).first()

    if check_id:
        check, model = check_car()

        if not check:
            release_year = int(input('Введите год машины: '))
            print()
            display_brand()
            my_id = int(input('Выберите ID бренда: '))
            brand = session.query(Brand).filter_by(id=my_id).first()
            update_car(car_id, {'model': model,
                                'release_year': release_year,
                                'brand': brand},
                       )
        else:
            raise WrongName
    elif car_id == 0:
        return

    else:
        raise IdError
    print()


def change_brand():
    print('Введите "0" для выхода в предыдущее меню.')
    brand_id = int(input('Выберите ID бренда, которую хотите изменить: '))

    if brand_id:
        check, name = check_brand()

        if not check:
            update_brand(brand_id, name)
        else:
            raise WrongName
    elif brand_id == 0:
        return
    else:
        raise IdError
    print()


def del_car():
    print('Введите "0" для выхода в предыдущее меню.')
    car_id = int(input('Введите ID машины, которую хотите удалить: '))

    if car_id != 0:
        check = session.query(Car).filter_by(id=car_id).first()

        if check:
            delete_car(car_id)
        else:
            raise IdError
    else:
        return
    print()


def del_brand():
    print('Введите "0" для выхода в предыдущее меню.')
    brand_id = int(input('Введите ID бренда, который хотите удалить: '))

    if brand_id != 0:
        check = session.query(Brand).filter_by(id=brand_id).first()

        if check:
            delete_brand(brand_id)
        else:
            raise IdError
    else:
        return
    print()


def functionality_car():
    while True:
        print('\nЕсли хотите просмотреть таблицу, выберите "1".\n'
              'Если хотите добавить запись в таблицу, выберите "2".\n'
              'Если хотите изменить запись в таблице, выберите "3".\n'
              'Если хотите удалить запись в таблице, выберите "4".\n'
              'Если хотите вернуться в предыдущее меню, выберите "0".\n')
        count = int(input('Ваш выбор: '))
        if count == 1:
            display_car()
        elif count == 2:
            add_car()
        elif count == 3:
            print()
            display_car()
            change_car()
        elif count == 4:
            print()
            display_car()
            del_car()
        elif count == 0:
            print('Выход в предыдущее меню.')
            break
        else:
            raise WrongChoice


def functionality_brand():
    while True:
        print('\nЕсли хотите просмотреть таблицу, выберите "1".\n'
              'Если хотите добавить запись в таблицу, выберите "2".\n'
              'Если хотите изменить запись в таблице, выберите "3".\n'
              'Если хотите удалить запись в таблице, выберите "4".\n'
              'Если хотите вернуться в предыдущее меню, выберите "0".\n')
        count = int(input('Ваш выбор: '))
        if count == 1:
            display_brand()
        elif count == 2:
            add_brand()
        elif count == 3:
            print()
            display_brand()
            change_brand()
        elif count == 4:
            print()
            display_brand()
            del_brand()
        elif count == 0:
            print('Выход в предыдущее меню.')
            break
        else:
            raise WrongChoice


def functionality_all():
    while True:
        print('Если хотите взаимодествовать с машинами, выберите "1".\n'
              'Если хотите взаимодествовать с брендами, выберите "2".\n'
              'Если хотите выйти, выберите "0".\n')
        count = int(input('Ваш выбор: '))
        if count == 1:
            functionality_car()
        elif count == 2:
            functionality_brand()
        elif count == 0:
            print('\nВыход')
            break
        else:
            raise WrongChoice
        print()


def main():
    pass


if __name__ == '__main__':
    main()
