from flask import Blueprint, render_template
from . import db

bp = Blueprint('pelicula', __name__, url_prefix='/peliculas')

@bp.route('/')
def Pelicula():
    consulta = """ 
        SELECT title, film_id FROM film 
        ORDER BY title ASC
"""

    con = db.get_db()
    res = con.execute(consulta)
    Peliculas = res.fetchall()
    pagina = render_template('peliculas.html',
                            Peliculas=Peliculas)
    return pagina

@bp.route('/')
def detalle(id):
    consulta = """ 
        SELECT description, rating, release_year, title, length FROM film 
        WHERE film_id = ?
"""
    con = db.get_db()
    res = con.execute(consulta,(id))
    Pelis= res.fetchall()

    consulta2 = """ 
        SELECT first_name, last_name, f.actor_id FROM film_actor f
        JOIN actor a ON a.actor_id = f.actor_id
        WHERE f.film_id = ?
"""
    res = con.execute(consulta2,(id))
    lista_actores= res.fetchall()
    paginaPelicula = render_template ('detallePeliculas.html',
                                     Pelis=Pelis,
                                     actores=lista_actores)
    
    return paginaPelicula