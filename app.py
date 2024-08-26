from flask import Flask, render_template, request
from strategies import get_suggested_numbers

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    suggested_numbers = None
    if request.method == 'POST':
        try:
            number = int(request.form.get('number'))
            if number < 0 or number > 36:
                raise ValueError("Número inválido")
            suggested_numbers = get_suggested_numbers(number)
        except ValueError:
            return render_template('index.html', error="Por favor, insira um número válido entre 0 e 36.")

    return render_template('index.html', suggested_numbers=suggested_numbers)


if __name__ == '__main__':
    app.run(debug=True)
