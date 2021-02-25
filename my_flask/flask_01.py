"""
Создать сайт. При запросе на домашнюю страницу отображается текущая дата.
"""

from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route('/')
def time_now():
    return f'{date.today()}'


if __name__ == '__main__':
    app.run()
