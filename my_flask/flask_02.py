"""
Создать сайт.
При запросе по урлу /two_pow/[number] возвращает 2 в степени number
"""

from flask import Flask

app = Flask(__name__)


@app.route('/two_pow/<int:number>')
def my_number(number):
    assert isinstance(number, int)
    return f'{number ** 2}'


if __name__ == '__main__':
    app.run()
