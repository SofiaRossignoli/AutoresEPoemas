from flask import Blueprint, render_template, request, redirect, flash
from models import Autor
from database import db

bp_autor = Blueprint('autor', __name__, template_folder="templates")

@bp_autor.route("/")
def index():
    a = Autor.query.all()
    return render_template("autores.html", autores=a)


@bp_autor.route("/add")
def add():
    return render_template("autores_add.html")


@bp_autor.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    pais = request.form.get("pais")

    if nome and pais:
        db_autor = Autor(nome, pais)
        db.session.add(db_autor)
        db.session.commit()
        flash("Autor salvo!")
        return redirect("/autores")
    else:
        flash("Preencha tudo!")
        return redirect("/autores/add")


@bp_autor.route("/remove/<int:id>")
def remove(id):
    a = Autor.query.get(id)
    try:
        db.session.delete(a)
        db.session.commit()
        flash("Autor removido!")
    except:
        flash("Autor inválido!")
    return redirect("/autores")


@bp_autor.route("/edit/<int:id>")
def edit(id):
    a = Autor.query.get(id)
    return render_template("autores_editar.html", autores=a)


@bp_autor.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    pais = request.form.get("pais")
    id_autor = request.form.get("id_autor")
    
    if nome and pais and id_autor:
        a = Autor.query.get(id_autor)
        a.nome = nome
        a.pais = pais
        db.session.commit()
        flash("Autor editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/autores")