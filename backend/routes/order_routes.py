from fastapi import APIRouter;

order_router = APIRouter(prefix="/orders", tags=["orders"]);

@order_router.get("/")
async def start():
    """
    Rota raiz da API de pedidos, retorna uma mensagem de boas-vindas.
    """
    return {"message": "API de pedidos está funcional!"}