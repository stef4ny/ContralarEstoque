from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.core.historico import obter_historico

router = APIRouter()

@router.get("/itens/{item_id}", response_class=HTMLResponse)
def detalhes_item(item_id: int):

    # 🔹 Obtém histórico real do item
    historico = obter_historico(item_id)

    # 🔹 Classifica tipo do evento (simples e eficiente)
    def tipo_evento(descricao: str):
        if "Pedido" in descricao:
            return "Pedido"
        if "Estoque" in descricao:
            return "Operação"
        if "Negociação" in descricao:
            return "Fornecedor"
        return "Sistema"

    # 🔹 Monta linhas da tabela
    if not historico:
        linhas = """
          <tr>
            <td colspan="3">Nenhum evento registrado.</td>
          </tr>
        """
    else:
        linhas = ""
        for data, descricao in historico:
            linhas += f"""
            <tr>
              <td>{data}</td>
              <td>{descricao}</td>
              <td>{tipo_evento(descricao)}</td>
            </tr>
            """

    return f"""
    <html>
      <head>
        <title>Detalhes do Item</title>
        <style>
          body {{
            font-family: Segoe UI, Arial, sans-serif;
            background: #f4f6f8;
            padding: 30px;
          }}
          .card {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            max-width: 900px;
            margin: auto;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
          }}
          h2 {{
            margin-top: 0;
          }}
          .section {{
            margin-top: 25px;
          }}
          .label {{
            color: #6b7280;
            font-size: 14px;
          }}
          .value {{
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 10px;
          }}
          ul {{
            padding-left: 20px;
          }}
          li {{
            margin-bottom: 10px;
          }}
          .btn {{
            display: inline-block;
            margin-top: 30px;
            background: #2563eb;
            color: white;
            padding: 10px 16px;
            border-radius: 6px;
            text-decoration: none;
          }}
        </style>
      </head>

      <body>

        <div class="card">
          <h2>📦 Detalhes do Item #{item_id}</h2>

          <div class="section">
            <div class="label">Produto</div>
            <div class="value">Fone de Ouvido ELG EP12BK</div>

            <div class="label">Risco</div>
            <div class="value">ALTO</div>

            <div class="label">Estimativa de Ruptura</div>
            <div class="value">Em 2 dias</div>
          </div>

          <div class="section">
            <h3>🕒 Histórico do Item</h3>
            <ul>
              {linhas}
            </ul>
          </div>

          <a class="btn" href="/dashboard">⬅ Voltar ao Dashboard</a>
        </div>

      </body>
    </html>
    """
 