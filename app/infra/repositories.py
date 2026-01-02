from sqlalchemy.orm import Session
from app.infra.models import RiscoRuptura
from app.infra.models import RiscoRuptura

from sqlalchemy import func, case
from app.infra.models import RiscoRuptura

def salvar_risco(
    db: Session,
    sku: str,
    vendas_ultima_hora: int,
    estoque_atual: int,
    risco: float
):
    registro = RiscoRuptura(
        sku=sku,
        vendas_ultima_hora=vendas_ultima_hora,
        estoque_atual=estoque_atual,
        risco=risco
    )
    db.add(registro)
    db.commit()
    db.refresh(registro)
    return registro

def buscar_historico_por_sku(
    db: Session,
    sku: str,
    limite: int = 50
):
    return (
        db.query(RiscoRuptura)
        .filter(RiscoRuptura.sku == sku)
        .order_by(RiscoRuptura.criado_em.desc())
        .limit(limite)
        .all()
    )


def buscar_alertas_recentes(db, limite: int = 10):
    return (
        db.query(RiscoRuptura)
        .filter(RiscoRuptura.risco >= 0.8)
        .order_by(RiscoRuptura.criado_em.desc())
        .limit(limite)
        .all()
    )

def contar_riscos(db):
    return {
        "alto": db.query(RiscoRuptura)
            .filter(RiscoRuptura.risco >= 0.8)
            .count(),

        "medio": db.query(RiscoRuptura)
            .filter(RiscoRuptura.risco >= 0.5, RiscoRuptura.risco < 0.8)
            .count(),

        "baixo": db.query(RiscoRuptura)
            .filter(RiscoRuptura.risco < 0.5)
            .count()
    }