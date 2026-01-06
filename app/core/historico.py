from datetime import datetime

# Histórico em memória (mock)
historico_itens = {}

def registrar_evento(item_id: int, descricao: str):
    evento = (
        datetime.now().strftime("%d/%m/%Y %H:%M"),
        descricao
    )

    historico_itens.setdefault(item_id, []).insert(0, evento)


def obter_historico(item_id: int):
    return historico_itens.get(item_id, [])
