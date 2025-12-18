
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