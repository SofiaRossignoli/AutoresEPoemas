from flask import Blueprint, render_template, request, redirect, flash
from models import Poema, Autor
from database import db

bp_poema = Blueprint('poema', __name__, template_folder="templates")

@bp_poema.route("/")
def index():
    p = Poema.query.all()
    return render_template("poemas.html", poemas=p)


@bp_poema.route("/add")
def add():
    a = Autor.query.all()
    return render_template("poemas_add.html", autores=a)


@bp_poema.route("/save", methods=['POST'])
def save():
    titulo = request.form.get("titulo")
    ano_publicacao = request.form.get("ano_publicacao")
    id_autor = request.form.get("id_autor")

    if titulo and ano_publicacao and id_autor:
        db_poema = Poema(titulo, ano_publicacao, id_autor)
        db.session.add(db_poema)
        db.session.commit()
        flash("Poema salvo!")
        return redirect("/poemas")
    else:
        flash("Preencha tudo!")
        return redirect("/poemas/add")


@bp_poema.route("/remove/<int:id>")
def remove(id):
    p = Poema.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Poema removido!")
    except:
        flash("Poema inválido!")
    return redirect("/poemas")


@bp_poema.route("/edit/<int:id>")
def edit(id):
    p = Poema.query.get(id)
    a = Autor.query.all()
    return render_template("poemas_editar.html", poema=p, alunos=a)


@bp_poema.route("/edit-save", methods=['POST'])
def edit_save():
    titulo = request.form.get("titulo")
    ano_publicacao = request.form.get("ano_publicacao")
    id_autor = request.form.get("id_autor")
    id_poema = request.form.get("id_poema")
    
    if titulo and ano_publicacao and id_poema and id_autor:
        p = Poema.query.get(id_poema)
        p.titulo = titulo
        p.ano_publicacao = ano_publicacao
        p.id_autor = id_autor
        db.session.commit()
        flash("Poema editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/poemas")