from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados PostgreSQL
# DATABASE_URL = "postgresql://postgres:1234@localhost/biblioteca"

# Configuração do banco de dados SQLite
DATABASE_URL = "sqlite:///biblioteca.db"

# Configuração do banco de dados MySQL
# DATABASE_URL = "mysql+pymysql://root:1234@localhost/biblioteca"

# Criação do motor e da base declarativa
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definição da classe Livro
class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

    def __repr__(self):
        return f"Livro(id={self.id}, titulo={self.titulo}, autor={self.autor}, preco={self.preco})"

# Definição da classe Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, email={self.email})"

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Funções CRUD para Livro
def adicionar_livro(titulo, autor, preco):
    novo_livro = Livro(titulo=titulo, autor=autor, preco=preco)
    session.add(novo_livro)
    session.commit()
    return novo_livro

def listar_livros():
    return session.query(Livro).all()

def atualizar_livro(id, titulo=None, autor=None, preco=None):
    livro = session.query(Livro).filter_by(id=id).one()
    if titulo:
        livro.titulo = titulo
    if autor:
        livro.autor = autor
    if preco:
        livro.preco = preco
    session.commit()
    return livro

def deletar_livro(id):
    livro = session.query(Livro).filter_by(id=id).one()
    session.delete(livro)
    session.commit()

# Funções CRUD para Usuario
def adicionar_usuario(nome, email):
    novo_usuario = Usuario(nome=nome, email=email)
    session.add(novo_usuario)
    session.commit()
    return novo_usuario

def listar_usuarios():
    return session.query(Usuario).all()

def atualizar_usuario(id, nome=None, email=None):
    usuario = session.query(Usuario).filter_by(id=id).one()
    if nome:
        usuario.nome = nome
    if email:
        usuario.email = email
    session.commit()
    return usuario

def deletar_usuario(id):
    usuario = session.query(Usuario).filter_by(id=id).one()
    session.delete(usuario)
    session.commit()

# Exemplo de uso
if __name__ == "__main__":
    # Adicionar exemplos
    adicionar_livro("1984", "George Orwell", 39.90)
    adicionar_usuario("Ana", "ana@example.com")

    # Listar todos
    print(listar_livros())
    print(listar_usuarios())

    # Atualizar um livro
    atualizar_livro(1, preco=42.0)

    # Deletar um usuário
    deletar_usuario(1)
