"""
Дан список имен, отфильтровать все имена, где есть буква o
[‘Kate’, ‘Kolya’, ‘Alex’] -> [‘Kolya’]
"""


def main():
    new_names = list(filter(lambda x: 'o' in x, ['Kate', 'Kolya', 'Alex']))
    print(new_names)


if __name__ == '__main__':
    main()
