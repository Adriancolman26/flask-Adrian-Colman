from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix='/lenguajes')

@bp. route('/')
def actor():
    consulta = """
     SELECT first_name,last_name FROM lenguaje
     ORDER BY first_name ;
 """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguajes = res.fetchall()
    pagina = render_template('lenguaje.html',
                            lenguaje=lista_lenguajes)
    return pagina