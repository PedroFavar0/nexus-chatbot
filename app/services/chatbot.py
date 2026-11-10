
from app.services.source_detection import identificarOrigem
from app.services.conversation import criarConversa, obterConversa


def processarMensagem(mensagem, conversaId=None, origem=None):

    conversa = obterConversa(conversaId) if conversaId else None

    if conversa is None:
        origem = identificarOrigem(origem)
        conversaId, conversa = criarConversa(origem)

        mensagemInicial = mensagem.lower().strip()

        saudacoes = [
            "oi",
            "olá",
            "ola",
            "bom dia",
            "boa tarde",
            "boa noite"
        ]

        if mensagemInicial not in saudacoes:
            conversa["necessidade"] = mensagem
            conversa["etapa"] = "aguardando_empresa"

            return {
                "conversa_id": conversaId,
                "origem": origem,
                "etapa": conversa["etapa"],
                "resposta": (
                    "Olá! Seja bem-vindo à Nexus Consultoria! "
                    "Entendi que você procura ajuda com: "
                    f"{mensagem}. Qual é o nome da sua empresa?"
                )
            }

        mensagensOrigem = {
            "instagram": (
                "Que bom ter você por aqui! "
                "Vimos que chegou pelo nosso Instagram."
            ),
            "x": (
                "Obrigado por chegar até nós pelo X!"
            ),
            "site": (
                "Obrigado por conhecer nossos serviços pelo site!"
            ),
            "direct": (
                "É um prazer receber seu contato!"
            )
        }

        resposta = (
            f"Olá! Seja bem-vindo à Nexus Consultoria! "
            f"{mensagensOrigem[origem]} "
            "Como podemos ajudar sua empresa hoje? "
            "Conte um pouco sobre sua necessidade."
        )

        return {
            "conversa_id": conversaId,
            "origem": origem,
            "etapa": conversa["etapa"],
            "resposta": resposta
        }

    if conversa["etapa"] == "aguardando_necessidade":
        conversa["necessidade"] = mensagem
        conversa["etapa"] = "aguardando_empresa"

        resposta = (
            "Entendi! Nossa equipe poderá avaliar essa necessidade. "
            "Qual é o nome da sua empresa?"
        )

    elif conversa["etapa"] == "aguardando_empresa":
        conversa["empresa"] = mensagem
        conversa["etapa"] = "qualificado"

        resposta = (
            f"Perfeito! Registrei sua empresa como {mensagem}. "
            "Obrigado pelas informações! "
            "Vamos encaminhar sua solicitação para nossa equipe comercial."
        )

    else:
        resposta = (
            "Sua solicitação já foi registrada! "
            "Nossa equipe comercial poderá dar continuidade ao atendimento."
        )

    return {
        "conversa_id": conversaId,
        "origem": conversa["origem"],
        "etapa": conversa["etapa"],
        "resposta": resposta
    }
