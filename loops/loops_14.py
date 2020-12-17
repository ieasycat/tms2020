"""
Создать список учеников подобной структуры.
Определить средний балл оценок по всем предметам,
и вывести сведения о студентах,
средний балл которых больше 4. [02-7.3-BL-02]
"""
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
summ = 0
for pupil in pupils:
    a = pupil['physics']
    b = pupil['informatics']
    c = pupil['history']
    name = pupil['firstname']
    summ = (a + b + c) / 3
    if summ > 4:
        print(f'У {name} средний бал {summ}')
