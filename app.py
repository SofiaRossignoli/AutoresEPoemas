from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha'
conexao = "mysql+pymysql://alunos@localhost:1406@127.0.0.1/autores"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Autor, Poema
db.init_app(app)
migrate = Migrate(app, db)

from modulos.autores.autores import bp_autor
app.register_blueprint(bp_autor, url_prefix='/autores')
from modulos.poemas.poemas import bp_poema
app.register_blueprint(bp_poema, url_prefix='/poemas')

@app.route("/")
def index():
    return render_template("index.html")