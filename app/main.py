from fastapi import FastAPI
from app.api.v1.endpoints import acoes, dashboard, health, estoque, itens

from app.infra.database import Base, engine
from app.infra import models
from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs.prever_ruptura import executar_previsao


app = FastAPI(title="Estoque Vivo MVP")

app.include_router(health.router)
app.include_router(estoque.router)
app.include_router(dashboard.router)
app.include_router(acoes.router)
app.include_router(itens.router)


Base.metadata.create_all(bind=engine)

scheduler = BackgroundScheduler()
scheduler.add_job(
    executar_previsao,
    trigger="interval",
    minutes=60  
)
scheduler.start()

