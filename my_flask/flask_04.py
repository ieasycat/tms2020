"""
Создать шаблон с формой Имя, фамилия, возраст.
Передать данные на вью дописать эти данные в файл
"""

from flask import Flask, url_for, redirect, request

app = Flask(__name__)


@app.route('/info', methods=['POST', 'GET'])
def info():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        old = request.form['old']
        return redirect(url_for(
            'success', first_name=first_name, last_name=last_name, old=old))
    else:
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        old = request.args.get('old')
        return redirect(url_for(
            'success', first_name=first_name, last_name=last_name, old=old))


@app.route('/success/<first_name>-<last_name>-<old>')
def success(first_name, last_name, old):
    with open('log_04.txt', 'a') as log_file:
        log_file.writelines([f'First name: {first_name}\n'
                             f'Last name: {last_name}\n'
                             f'Old: {old}\n\n'])
    return f'Welcome {last_name} {first_name}. ' \
           f'You old: {old}'


if __name__ == '__main__':
    app.run()


# Запуск
# http://127.0.0.1:5000/info?first_name=Anton&last_name=Klimenka&old=28
# http://127.0.0.1:5000/success/Roman-Loiko-29
