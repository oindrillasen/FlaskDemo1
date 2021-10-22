from flask import Flask, render_template, request
from pip._vendor import requests

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
            num1 = request.form['num1']
            num2 = request.form['num2']
            operation = request.form['operation']

            if operation == 'add':
                result = float(num1) + float(num2)
                return render_template('app.html', result=result)

            elif operation == 'subtract':
                result = float(num1) - float(num2)
                return render_template('app.html', result=result)

            elif operation == 'multiply':
                result = float(num1) * float(num2)
                return render_template('app.html', result=result)

            elif operation == 'divide':
                result = float(num1) / float(num2)
                return render_template('app.html', result=result)
            else:
                return render_template('app2.html')



if __name__ == ' __main__':
    app.debug = True
    app.run()