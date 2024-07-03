from flask import Blueprint, render_template
from . import db

bp = Blueprint('categoria', __name__, url_prefix='/categorias')

@bp.route('/')
def categoria():
    consulta = """
     SELECT name, category_id FROM category
     ORDER BY name ASC ; 
"""
    con = db.get_db()
    res = con.execute(consulta)
    lista_categorias = res.fetchall()
    pagina = render_template('category.html',
                            categorias=lista_categorias)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta = """
        SELECT name, category_id FROM category
        WHERE category_id = ?
    """

    con = db.get_db()
    res = con.execute(consulta, (id,))
    categoria = res.fetchone()
    
    consulta2 = """
        SELECT f.title as titulo,  c.category_id FROM film f
        JOIN film_category fi on fi.film_id = f.film_id
        JOIN category c on c.category_id = fi.category_id
        WHERE c.category_id = ?
    """

    res = con.execute(consulta2, (id,))
    lista_peliculas = res.fetchall()
    paginaLenguaje = render_template("detallesCategoria.html",
                                  categorias = categoria,
                                  peliculas=lista_peliculas)
    return paginaLenguaje