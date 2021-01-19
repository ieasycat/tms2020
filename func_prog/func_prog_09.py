"""
Дан список строк.
Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""


def main():
    listt = [f'{i} - {k}'
             for i, k in enumerate(['Alo', 'Hello', 'Man', 'Good'], 1)]
    print(listt)


if __name__ == '__main__':
    main()
