import datetime
from xmlrpc.client import DateTime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker # type: ignore
from sqlalchemy_utils import ChoiceType # type: ignore

db = create_engine("sqlite:///database/banco.db", connect_args={"check_same_thread": False})

Base = declarative_base()


SessionLocal = sessionmaker(bind=db, autocommit=False, autoflush=False)

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



# Usuario, Pedido, ItensPedido

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    nome = Column("nome", String, nullable=False, index=True)
    email = Column("email", String, unique=True, nullable=False, index=True)
    cpf = Column("cpf", String, unique=True, nullable=False, index=True)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome: str, email: str, cpf: str, senha: str, ativo: bool = True, admin: bool = False):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

    
class Pedido(Base):
    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )
    __tablename__ = "pedidos"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    status = Column("status", String, nullable=False, index=True)
    usuario = Column("usuario", Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    preco = Column("preco", Float, nullable=False)
    # data_criacao = Column("data_criacao", DateTime, default=datetime.now)

    def __init__(self, usuario, status = "PENDENTE", preco = 0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
class ItensPedido(Base):
    __tablename__ = "itens_pedido"
    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

Base.metadata.create_all(db)
