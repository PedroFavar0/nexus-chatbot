
def identificarOrigem(origem):
    origens = {
        "instagram": "instagram",
        "ig": "instagram",
        "x": "x",
        "twitter": "x",
        "site": "site",
        "website": "site",
        "direct": "direct",
        "direto": "direct"
    }

    origemNormalizada = origem.lower().strip() if origem else "direct"

    return origens.get(origemNormalizada, "direct")
