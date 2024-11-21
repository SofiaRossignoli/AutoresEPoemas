from database import db

class Autor(db.Model):
    __tablename__ = 'autores'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.Varchar(100))
    pais = db.Column(db.Varchar(50))
   
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
    
    def __repr__(self):
        return f"<Autor {self.nome}>"
    

class Poema(db.Model):
    __tablename__ = 'poemas'
    id_poema = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.Varchar(100))
    ano_publicacao = db.Column(db.Int)
    id_autor = db.Column(db.Integer, db.ForeignKey('alunos.id_autor'))

    autor = db.relationship('Autor', foreign_keys=id_autor)

    def __init__(self, titulo, ano_publicacao, id_autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.id_autor = id_autor
    
    def __repr__(self):
        return f"<Cadastro: {self.titulo} - {self.ano_publicacao} - {self.id_autor}> "