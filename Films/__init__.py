from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/Boca')
def Boca():
    return 'Boca el mas grande de todos'

with app.app_context():
   from . import db
   db.init_app(app)

from . import actor
app.register_blueprint(actor.bp)

from . import lenguaje
app.register_blueprint(lenguaje.bp)
