"""
Создать список учеников подобной структуры.
Определить средний балл оценок по всем предметам,
и вывести сведения о студентах,
средний балл которых больше 4. [02-7.3-BL-02]
"""


def average_rating(learner):
    for pupil in learner:
        summ = 0
        a = pupil['physics']
        b = pupil['informatics']
        c = pupil['history']
        name = pupil['firstname']
        summ = (a + b + c) / 3
        if summ > 4:
            print(f'У {name} средний бал {summ}')


def main():
    pupils = [
        {
            'firstname': 'Masha',
            'Group': 42,
            'physics': 7,
            'informatics': 6,
            'history': 8,
        },
        {
            'firstname': 'Anton',
            'Group': 42,
            'physics': 7,
            'informatics': 8,
            'history': 5,
        },
        {
            'firstname': 'Dima',
            'Group': 43,
            'physics': 5,
            'informatics': 6,
            'history': 5,
        },
    ]
    average_rating(pupils)


if __name__ == '__main__':
    main()
