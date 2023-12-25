from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        user_data = request.form.get('data')
        if user_data:
            print(f'Полученные даные: {user_data}')
        else:
            print('Ошибка. Некорректные данные в форме')\

    return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)