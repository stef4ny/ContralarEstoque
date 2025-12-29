from fastapi import APIRouter
from app.domain.services import calcular_risco_ruptura
from app.infra.database import SessionLocal
from app.infra.repositories import salvar_risco
from app.schemas.estoque import HistoricoRiscoResponse
from app.infra.repositories import buscar_historico_por_sku
from typing import List

router = APIRouter()

@router.get("/risco")
def risco_ruptura(
    sku: str,
    vendas_ultima_hora: int,
    estoque_atual: int
):
    risco = calcular_risco_ruptura(
        vendas_ultima_hora=vendas_ultima_hora,
        estoque_atual=estoque_atual
    )

    db = SessionLocal()
    salvar_risco(
        db=db,
        sku=sku,
        vendas_ultima_hora=vendas_ultima_hora,
        estoque_atual=estoque_atual,
        risco=risco
    )
    db.close()

    return {
        "sku": sku,
        "risco": risco,
        "classificacao": (
            "ALTO" if risco >= 0.8
            else "MEDIO" if risco >= 0.5
            else "BAIXO"
        )
    }


@router.get(
    "/historico/{sku}",
    response_model=List[HistoricoRiscoResponse]
)
def historico_risco(
    sku: str,
    limite: int = 20
):
    db = SessionLocal()
    registros = buscar_historico_por_sku(
        db=db,
        sku=sku,
        limite=limite
    )
    db.close()
    return registros
