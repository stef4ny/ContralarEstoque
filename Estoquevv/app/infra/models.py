from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.infra.database import Base

class RiscoRuptura(Base):
    __tablename__ = "risco_ruptura"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, index=True)
    vendas_ultima_hora = Column(Integer)
    estoque_atual = Column(Integer)
    risco = Column(Float)
    criado_em = Column(DateTime, default=datetime.utcnow)
