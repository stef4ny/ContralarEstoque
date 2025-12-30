from app.domain.services import calcular_risco_ruptura
from app.domain.rules import deve_alertar
from app.infra.database import SessionLocal
from app.infra.repositories import salvar_risco
from app.infra.integrations.notificacao import send_notification

SKUS_MONITORADOS = [
    {"sku": "SKU123", "vendas": 5, "estoque": 8},
    {"sku": "SKU456", "vendas": 2, "estoque": 20},
    {"sku": "SKU789", "vendas": 10, "estoque": 6},
]

def executar_previsao():
    print("🔁 Executando job de previsão de ruptura")

    db = SessionLocal()

    for item in SKUS_MONITORADOS:
        risco = calcular_risco_ruptura(
            vendas_ultima_hora=item["vendas"],
            estoque_atual=item["estoque"]
        )

        salvar_risco(
            db=db,
            sku=item["sku"],
            vendas_ultima_hora=item["vendas"],
            estoque_atual=item["estoque"],
            risco=risco
        )

        print(f"📦 SKU {item['sku']} | Risco {risco}")

        if deve_alertar(risco):
            send_notification(item["sku"], risco)

    db.close()
    print("✅ Job de previsão de ruptura concluído")