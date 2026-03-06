
from fastapi import APIRouter, Depends, HTTPException, status
from models import Usuario, get_db # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def start():
    """
    Rota raiz da API de autenticação, retorna uma mensagem de boas-vindas.
    """
    return {"message": "API de autenticação está funcional!"}

@auth_router.post("/criar")
async def criar_conta(nome: str, email: str, senha: str, cpf: str, session = Depends(get_db)):
    

    usuario = session.query(Usuario).filter(Usuario.email == email).first() # type: ignore
    if usuario:
        return {"message": "Email já cadastrado."}
    else:
        novo_usuario = Usuario(nome, email, cpf, senha) # type: ignore
        session.add(novo_usuario) # type: ignore
        session.commit() # type: ignore
        return {"message": "Conta criada com sucesso!"}