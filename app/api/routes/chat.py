
from fastapi import APIRouter

from app.schemas.message import ChatRequest, ChatResponse
from app.services.chatbot import processarMensagem


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def conversar(dados: ChatRequest):

    resultado = processarMensagem(
        mensagem=dados.mensagem,
        conversaId=dados.conversa_id,
        origem=dados.origem
    )

    return resultado
