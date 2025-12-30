import smtplib
from email.message import EmailMessage
from app.core.config import settings
from datetime import datetime, timedelta

def send_notification(sku: str, risco: float):
    agora = datetime.utcnow()



    COOLDOWN_MINUTOS = 60 


    if sku in ultimo_envio:
        diferenca = agora - ultimo_envio[sku]
        if diferenca < timedelta(minutes=COOLDOWN_MINUTOS):
            print(f"⏳ Alerta ignorado (cooldown ativo) | Item {sku}")
            return


    ultimo_envio[sku] = agora

    msg = EmailMessage()
    msg["Subject"] = f"🚨 Alerta de Ruptura – Item {sku}"
    msg["From"] = settings.EMAIL_USER
    msg["To"] = settings.EMAIL_TO

    msg.set_content(
        f"""
ALERTA DE RUPTURA DETECTADO

Item: {sku}
Risco estimado: {risco}

Ação recomendada:
Verificar reposição imediata.
"""
    )

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        server.send_message(msg)

    print(f"📧 Email enviado | Item {sku}")

