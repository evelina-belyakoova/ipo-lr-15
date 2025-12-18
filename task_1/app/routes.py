
from flask import request
from flask import Blueprint

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return 'Привet'

@main.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'

@main.route('/square/<int:number>')
def square(number):
    return f'Квадрат числа {number} равен {number ** 2}'

@main.route('/json', methods=['POST'])
def json():
    data = request.get_json()

    if not data or 'name' not in data or 'age' not in data:
        print(f"Некорректные данные")

    name = data['name']
    age = data['age']
    return jsonify({"message": f"Привет, {name}! Тебе {age} лет."})

@main.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return f"Произведение чисел {a} и {b} равно {a * b}"