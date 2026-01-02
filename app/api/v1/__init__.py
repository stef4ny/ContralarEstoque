from fastapi import APIRouter

from .endpoints import health, estoque, alertas, acoes

router = APIRouter()

router.include_router(health.router, prefix="", tags=["health"])
router.include_router(estoque.router, prefix="/estoque", tags=["estoque"])
router.include_router(alertas.router, prefix="/alertas", tags=["alertas"])
router.include_router(acoes.router)

