import smtplib
from email.message import EmailMessage
from app.core.config import settings


def send_notification(sku: str, risco: float):
    # 1️⃣ Criar a mensagem
    msg = EmailMessage()
    msg["Subject"] = f"🚨 Alerta de Ruptura – SKU {sku}"
    msg["From"] = settings.EMAIL_USER
    msg["To"] = settings.EMAIL_TO

    msg.set_content(
        f"""
ALERTA DE RUPTURA DETECTADO

SKU: {sku}
Risco estimado: {risco}

Ação recomendada:
Verificar reposição imediata.

— Estoque Vivo MVP
"""
    )

    # 2️⃣ Enviar o email
    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        server.send_message(msg)

    print(f"📧 Email enviado com sucesso | SKU {sku}")
