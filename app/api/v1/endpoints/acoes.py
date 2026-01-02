from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse



router = APIRouter(prefix="/acoes", tags=["Ações"])


@router.get("/aumentar-pedido", response_class=HTMLResponse)
def aumentar_pedido(item: int = Query(...)):
    return f"""
    <html>
      <head>
        <title>Aumentar Pedido</title
      </head>
      <body>
        <h1>📦 Aumentar Pedido</h1>

        <p><strong>Item selecionado:</strong> {item}</p>

        <p>
          Esta ação irá aumentar o pedido para este item,
          reduzindo o risco de ruptura.
        </p>

        <ul>
          <li>Impacto: Reduz risco</li>
          <li>Custo estimado: Médio</li>
          <li>Prazo médio: 3 dias</li>
        </ul>

        <button>Confirmar ação</button>
        <br><br>
        <a href="/dashboard">⬅ Voltar ao dashboard</a>
      </body>
    </html>
    """
