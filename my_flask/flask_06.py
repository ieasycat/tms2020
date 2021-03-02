"""
Создать шаблон flask_06_form.html.
C формой Имя, фамилия, возраст.
Создать вью /form: при GET запросе отображать форму,
при POST запросе Выводить данные пользователю
с помощью шаблона flask_06_display.html
"""

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('flask_06_form.html')
    else:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        old = request.form.get('old')
        user = {'firstname': first_name,
                'lastname': last_name,
                'old': old}
        return render_template('flask_06_display.html', user=user)


if __name__ == '__main__':
    app.run()
