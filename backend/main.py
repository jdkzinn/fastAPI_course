from fastapi import APIRouter, FastAPI
# uvicorn main:app --reload
app = FastAPI(title="Curso de FastAPI", version="1.0.0", description="API de exemplo para curso de FastAPI");

from routes.auth_routes import auth_router
from routes.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

@app.get("/")
async def root():

    """
    Rota raiz da API, retorna uma mensagem de boas-vindas."""
    return {"message": "API está Funcional!"}

@app.get("/health")
async def health_check():
    """
    Rota de verificação de saúde da API, retorna o status da API.
    """
    return {"status": "API está saudável!"}

