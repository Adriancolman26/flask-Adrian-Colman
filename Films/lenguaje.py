from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix='/lenguajes')

@bp.route('/')
def lenguaje():
    consulta = """
     SELECT name, language_id FROM language
     ORDER BY name ASC ; 
"""
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguajes = res.fetchall()
    pagina = render_template('lenguaje.html',
                            lenguajes=lista_lenguajes)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT name, language_id FROM language
        WHERE language_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    lenguaje = res.fetchone()
    consulta2 = """
        SELECT f.title as titulo, l.language_id FROM film f
        JOIN language l on l.language_id = f.language_id
        WHERE l.language_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaLenguaje = render_template("detallesLenguaje.html",
                                  lenguaje=lenguaje,
                                  peliculas=lista_peliculas)
    return paginaLenguaje