from fastapi import APIRouter;

auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
async def start():
    """
    Rota raiz da API de autenticação, retorna uma mensagem de boas-vindas.
    """
    return {"message": "API de autenticação está funcional!"}

