from fastapi import APIRouter

from app.schemas.alertas import Alert
from app.infra.integrations.notificacao import send_notification


router = APIRouter()


@router.post("/", status_code=201)
async def create_alert(alert: Alert):
    # send notification (stub)
    send_notification(alert.dict())
    return {"ok": True}
