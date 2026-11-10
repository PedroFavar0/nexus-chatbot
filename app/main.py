
from fastapi import FastAPI
from app.api.routes.chat import router as chatRouter


app = FastAPI(
    title="Nexus Consultoria",
    description="API de atendimento inteligente da Nexus Consultoria",
    version="1.0.0"
)


app.include_router(chatRouter, prefix="/api")


@app.get("/")
def inicio():
    return {
        "empresa": "Nexus Consultoria",
        "mensagem": "Bem-vindo à nossa API!",
        "status": "online"
    }


@app.get("/health")
def verificarSaude():
    return {
        "status": "healthy"
    }
