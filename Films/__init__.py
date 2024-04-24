from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/Boca')
def Boca():
    return 'Boca el mas grande de todos'

