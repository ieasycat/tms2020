from cars.car import Brand, Car, session


class WrongChoice(Exception):
    def __init__(self, message='Такого выбора нет!'):
        super(WrongChoice, self).__init__(message)


class IdError(Exception):
    def __init__(self, message='Такого ID нет!'):
        super(IdError, self).__init__(message)


class WrongName(Exception):
    def __init__(self, message='Такое название уже есть!'):
        super(WrongName, self).__init__(message)


def create_car(values):
    car = Car(**values)
    session.add(car)
    session.commit()


def read_car():
    cars = session.query(Car).all()
    return cars


def update_car(car_id, new_value):
    car = session.query(Car).filter(Car.id == car_id).first()
    car.model = new_value['model']
    car.release_year = new_value['release_year']
    session.add(car)
    session.commit()


def delete_car(car_id):
    session.query(Car).filter(Car.id == car_id).delete()
    session.commit()


def create_brand(name):
    brand = Brand(**name)
    session.add(brand)
    session.commit()


def read_brand():
    brands = session.query(Brand).all()
    return brands


def update_brand(brand_id, new_name):
    brand = session.query(Brand).filter(Brand.id == brand_id).first()
    brand.name = new_name
    session.add(brand)
    session.commit()


def delete_brand(brand_id):
    session.query(Car.brand_id).filter_by(brand_id=brand_id).delete()
    session.query(Brand).filter(Brand.id == brand_id).delete()
    session.commit()


def main():
    pass


if __name__ == '__main__':
    main()
