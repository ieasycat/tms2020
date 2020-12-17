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
tmp = {}
for i in pupils:
    tmp = pupils[i]
    if 'physics' in tmp.keys():
        a = tmp['physics']
        if 'informatics' in tmp.keys():
            b = tmp['informatics']
            if 'history' in tmp.keys():
                c = tmp['history']
    name = tmp['firstname']
    summ = (a + b + c) / 3
    if summ > 4:
        print(f'У {name} средний бал {summ}')
