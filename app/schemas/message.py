
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    mensagem: str = Field(min_length=1, max_length=2000)
    conversa_id: str | None = None
    origem: str | None = "direct"


class ChatResponse(BaseModel):
    conversa_id: str
    origem: str
    etapa: str
    resposta: str
