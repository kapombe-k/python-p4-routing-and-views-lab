#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:username>')
def print_string(username):
    print(f'This is the print page {username}')
    return f'Welcome to the print page, {username}'

@app.route('/count/<int:number>')
def count(number):
    countdown_numbers=list(range(0, number+1))
    return countdown_numbers

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            error_message = "Error: Division by zero is not allowed."
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            error_message = "Error: Modulus by zero is not allowed."
    else:
        error_message = f"Error: Invalid operation '{operation}'. Supported operations are +, -, *, div, %."
    
    return (result, error_message)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
