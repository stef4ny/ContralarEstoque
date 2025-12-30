from pydantic import BaseModel
from typing import List
from datetime import datetime

class StockItem(BaseModel):
    sku: str
    store: str
    quantity: int


class ForecastRequest(BaseModel):
    days: int = 7
    stores: List[str] | None = None


class ForecastResponse(BaseModel):
    at_risk: List[StockItem]
    model: str

class HistoricoRiscoResponse(BaseModel):
    sku: str
    vendas_ultima_hora: int
    estoque_atual: int
    risco: float
    criado_em: datetime

    class Config:
        from_attributes = True