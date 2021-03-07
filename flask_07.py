"""
Создать ветку flask_school от мастера.
Описать модель группы(id, fullname).
Создать сайт. Создать напрямую в базе 3 группы.
Описать шаблон и вью для получения и отображения списка всех групп.
Создать шаблон и вью для создания группы.
Добавить ссылку для перехода на создание группы
на страницу отображения всех групп.
"""

from flask import Flask, request, render_template, url_for, \
    redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(50))


db.init_app(app)
db.create_all()


@app.route('/info')
def info():
    groups = Group.query.all()
    return render_template('display_all.html', groups=groups)


@app.route('/create_group', methods=['POST', 'GET'])
def create_group():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        group = Group(fullname=fullname)
        db.session.add(group)
        db.session.commit()
        db.session.close()
        return redirect(url_for('info'))
    else:
        return render_template('create_group.html')


@app.route('/change_group/<int:my_id>', methods=['POST', 'GET'])
def change_group(my_id):
    group = Group.query.filter(Group.id == my_id).first()
    if request.method == 'POST':
        group.fullname = request.form.get('fullname')
        db.session.add(group)
        db.session.commit()
        db.session.close()
        return redirect(url_for('info'))
    else:
        return render_template('change_group.html', group=group)


@app.route('/del_group/<int:my_id>')
def del_group(my_id):
    Group.query.filter(Group.id == my_id).delete()
    db.session.commit()
    db.session.close()
    return redirect(url_for('info'))
