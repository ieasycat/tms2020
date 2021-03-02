"""
Создать ветку flask_school от мастера.
Описать модель группы(id, fullname).
Создать сайт. Создать напрямую в базе 3 группы.
Описать шаблон и вью для получения и отображения списка всех групп.
Создать шаблон и вью для создания группы.
Добавить ссылку для перехода на создание группы
на страницу отображения всех групп.
"""

from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///school.db'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(50))


db.init_app(app)
db.create_all()


@app.route('/info', methods=['GET'])
def info():
    groups = Group.query.all()
    return render_template('display_all.html', groups=groups)


@app.route('/create_group', methods=['POST', 'GET'])
def create_group():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        group = Group(fullname=first_name)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('info'))
    else:
        return render_template('create_group.html')


if __name__ == '__main__':
    app.run(port=8000)
