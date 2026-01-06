from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse
from app.core.historico import registrar_evento



router = APIRouter(prefix="/acoes", tags=["Ações"])


@router.get("/aumentar-pedido/{item}", response_class=HTMLResponse)
def aumentar_pedido(item: int):
    


    registrar_evento(
        item,
        "Pedido aumentado manualmente pelo usuário"
    )


  

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


      <body style="font-family:Arial; 
                   padding:40px;">

        <h2>✅ Pedido aumentado com sucesso</h2>
        <p>Item: {item}</p>
        <a href="/itens/{item}"><button>Ver histórico do item</button></a><br><br>
        <a href="/dashboard"><button>Voltar ao dashboard</button></a>
        <br><br>
        <button>Confirmar ação</button>

        
      </body>
      </body>
    </html>
    """



@router.get("/realocar-estoque/{item_id}", response_class=HTMLResponse)
def realocar_estoque(item_id: int):

    registrar_evento(
        item_id,
        "Estoque realocado entre unidades"
    )

    return f"""
    <html>
      <body style="font-family:Arial; padding:40px;">
        <h2>🔄 Estoque realocado com sucesso</h2>
        <p>Item: {item_id}</p>

        <a href="/itens/{item_id}">📦 Ver histórico do item</a><br><br>
        <a href="/dashboard">⬅ Voltar ao dashboard</a>
      </body>
    </html>
    """

@router.get("/negociar-fornecedor/{item_id}", response_class=HTMLResponse)
def negociar_fornecedor(item_id: int):

    registrar_evento(
        item_id,
        "Negociação iniciada com fornecedor"
    )

    return f"""
    <html>
      <body style="font-family:Arial; padding:40px;">
        <h2>🤝 Negociação iniciada</h2>
        <p>Item: {item_id}</p>

        <a href="/itens/{item_id}">📦 Ver histórico do item</a><br><br>
        <a href="/dashboard">⬅ Voltar ao dashboard</a>
      </body>
    </html>
    """