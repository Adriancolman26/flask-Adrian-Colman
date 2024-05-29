from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix='/lenguajes')

@db. route('/lenguaje')
def lenguaje():
    consulta = """
     SELECT name FROM lenguage
     ORDER BY name ASC; 
     """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguajes = res.fetchall()
    pagina = render_template('lenguaje.html',
                            lenguaje=lista_lenguajes)
    return pagina