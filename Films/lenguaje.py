from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje', __name__, url_prefix='/lenguajes')

@bp.route('/')
def lenguaje():
    consulta = """
     SELECT name FROM language
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
        SELECT name FROM language
        WHERE lenguage_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    lista_lenguajes = res.fetchone()
    consulta2 = """
        SELECT title as titulo, f.film_id FROM film f
        JOIN film_actor fil on f.film_id = fil.film_id
        WHERE fil.actor_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaLenguaje = render_template("detallesLengz.html",
                                  lista_lenguajes=lista_lenguajes,
                                  peliculas=lista_peliculas)
    return paginaLenguaje