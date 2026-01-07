from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.core.historico import registrar_evento, obter_historico

router = APIRouter(prefix="/acoes", tags=["Ações"])


@router.get("/aumentar-pedido/{item_id}", response_class=HTMLResponse)
def aumentar_pedido(item_id: int):

    # 🔹 Registra evento no histórico
    registrar_evento(
        item_id,
        "Pedido aumentado manualmente pelo usuário"
    )

    # 🔹 Busca histórico atualizado
    historico = obter_historico(item_id)

    # 🔹 Classificação simples de evento
    def tipo_evento(descricao: str):
        if "Pedido" in descricao:
            return "Pedido"
        if "Estoque" in descricao:
            return "Operação"
        if "Negociação" in descricao:
            return "Fornecedor"
        return "Sistema"

    # 🔹 Monta tabela
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

    # 🔹 HTML final (mesma estrutura visual)
    return HTMLResponse(f"""
    <html>
      <head>
        <title>Aumentar Pedido</title>
        <style>
          body {{
            font-family: "Segoe UI", Arial, sans-serif;
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

          .success {{
            background: #ecfdf5;
            border: 1px solid #10b981;
            padding: 15px;
            border-radius: 6px;
            color: #065f46;
            margin-bottom: 25px;
            font-weight: 500;
          }}

          .historico-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
          }}

          .historico-table th {{
            background: #f3f4f6;
            text-align: left;
            padding: 10px;
            font-size: 13px;
            color: #374151;
          }}

          .historico-table td {{
            padding: 10px;
            border-top: 1px solid #e5e7eb;
            font-size: 14px;
          }}

          .btn {{
            display: inline-block;
            margin-top: 30px;
            background: #2563eb;
            color: white;
            padding: 10px 16px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 14px;
          }}
        </style>
      </head>

      <body>

        <div class="card">
          <h2>📦 Pedido Aumentado</h2>

          <div class="success">
            ✔ Pedido do item <strong>#{item_id}</strong> foi aumentado com sucesso.
          </div>

          <h3>🕒 Histórico do Item</h3>

          <table class="historico-table">
            <thead>
              <tr>
                <th>Data / Hora</th>
                <th>Evento</th>
                <th>Tipo</th>
              </tr>
            </thead>
            <tbody>
              {linhas}
            </tbody>
          </table>

          <a class="btn" href="/dashboard">⬅ Voltar ao Dashboard</a>
        </div>

      </body>
    </html>
    """)






@router.get("/realocar-estoque/{item_id}", response_class=HTMLResponse)
def realocar_estoque(item_id: int):

    # 🔹 Registra evento no histórico
    registrar_evento(
        item_id,
        "Estoque realocado manualmente pelo usuário"
    )

    # 🔹 Busca histórico atualizado
    historico = obter_historico(item_id)

    # 🔹 Classificação simples do tipo de evento
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

    # 🔹 HTML final
    return HTMLResponse(f"""
    <html>
      <head>
        <title>Realocar Estoque</title>
        <style>
          body {{
            font-family: "Segoe UI", Arial, sans-serif;
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

          .success {{
            background: #eff6ff;
            border: 1px solid #3b82f6;
            padding: 15px;
            border-radius: 6px;
            color: #1e3a8a;
            margin-bottom: 25px;
            font-weight: 500;
          }}

          .historico-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
          }}

          .historico-table th {{
            background: #f3f4f6;
            text-align: left;
            padding: 10px;
            font-size: 13px;
            color: #374151;
          }}

          .historico-table td {{
            padding: 10px;
            border-top: 1px solid #e5e7eb;
            font-size: 14px;
          }}

          .btn {{
            display: inline-block;
            margin-top: 30px;
            background: #2563eb;
            color: white;
            padding: 10px 16px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 14px;
          }}
        </style>
      </head>

      <body>

        <div class="card">
          <h2>📦 Estoque Realocado</h2>

          <div class="success">
            ✔ Estoque do item <strong>#{item_id}</strong> foi realocado com sucesso.
          </div>

          <h3>🕒 Histórico do Item</h3>

          <table class="historico-table">
            <thead>
              <tr>
                <th>Data / Hora</th>
                <th>Evento</th>
                <th>Tipo</th>
              </tr>
            </thead>
            <tbody>
              {linhas}
            </tbody>
          </table>

          <a class="btn" href="/dashboard">⬅ Voltar ao Dashboard</a>
        </div>

      </body>
    </html>
    """)




@router.get("/negociar-fornecedor/{item_id}", response_class=HTMLResponse)
def negociar_fornecedor(item_id: int):

    # 🔹 Registra evento no histórico
    registrar_evento(
        item_id,
        "Negociação iniciada com fornecedor"
    )

    # 🔹 Busca histórico atualizado
    historico = obter_historico(item_id)

    # 🔹 Classificação do tipo de evento
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

    # 🔹 HTML final
    return HTMLResponse(f"""
    <html>
      <head>
        <title>Negociar com Fornecedor</title>
        <style>
          body {{
            font-family: "Segoe UI", Arial, sans-serif;  
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

          .success {{
            background: #fff7ed;
            border: 1px solid #f97316;
            padding: 15px;
            border-radius: 6px;
            color: #9a3412;
            margin-bottom: 25px;
            font-weight: 500;
          }}

          .historico-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
          }}

          .historico-table th {{
            background: #f3f4f6;
            text-align: left;
            padding: 10px;
            font-size: 13px;
            color: #374151;
          }}

          .historico-table td {{
            padding: 10px;
            border-top: 1px solid #e5e7eb;
            font-size: 14px;
          }}

          .btn {{
            display: inline-block;
            margin-top: 30px;
            background: #2563eb;
            color: white;
            padding: 10px 16px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 14px;
          }}
        </style>
      </head>

      <body>

        <div class="card">
          <h2>🤝 Negociação com Fornecedor</h2>

          <div class="success">
            ✔ Negociação iniciada para o item <strong>#{item_id}</strong>.
          </div>

          <h3>🕒 Histórico do Item</h3>

          <table class="historico-table">
            <thead>
              <tr>
                <th>Data / Hora</th>
                <th>Evento</th>
                <th>Tipo</th>
              </tr>
            </thead>
            <tbody>
              {linhas}
            </tbody>
          </table>

          <a class="btn" href="/dashboard">⬅ Voltar ao Dashboard</a>
        </div>

      </body>
    </html>
    """)
