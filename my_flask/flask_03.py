"""
Создать сайт.
При запросе по урлу /my_word/[word],
в случае если длина слова четна - выводит строку содержащую
все нечетные элементы строки(abcde -> ace).
В ином случае перенаправлять на домашнюю страницу.
"""

from flask import Flask, url_for, redirect
from datetime import date

app = Flask(__name__)


@app.route('/my_word/<string:word>')
def func_word(word):
    assert isinstance(word, str)
    if len(word) % 2 == 0:
        return f' Hello {word[::2]}!'
    else:
        return redirect(url_for('time_now'))


@app.route('/')
def time_now():
    return f'{date.today()}'


if __name__ == '__main__':
    app.run()
