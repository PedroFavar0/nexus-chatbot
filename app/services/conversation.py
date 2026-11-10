
from uuid import uuid4

conversas = {}


def criarConversa(origem):
    conversaId = str(uuid4())

    conversas[conversaId] = {
        "origem": origem,
        "etapa": "aguardando_necessidade",
        "necessidade": None,
        "empresa": None
    }

    return conversaId, conversas[conversaId]


def obterConversa(conversaId):
    return conversas.get(conversaId)
