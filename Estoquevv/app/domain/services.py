def calcular_risco_ruptura(vendas_ultima_hora: int, estoque_atual: int):
    if estoque_atual <= 0:
        return 1.0

    consumo_por_hora = vendas_ultima_hora
    horas_restantes = estoque_atual / max(consumo_por_hora, 1)

    if horas_restantes < 2:
        return 0.9
    elif horas_restantes < 6:
        return 0.6
    else:
        return 0.2
