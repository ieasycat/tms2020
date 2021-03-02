"""
Создать папку templates в корне проекта.
Создать шаблон flask_05.html с формой Имя, фамилия, возраст.
Создать вью /form: при GET запросе отображать форму,
при POST запросе дописывать переданные данные в файл.
"""

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../templates')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('flask_05.html')
    else:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        old = request.form.get('old')
        with open('log_05.txt', 'a') as log_file:
            log_file.writelines([f'First name: {first_name}\n'
                                 f'Last name: {last_name}\n'
                                 f'Old: {old}\n\n'])
        return 'Success'


if __name__ == '__main__':
    app.run()
