from app.infra.database import SessionLocal
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app.infra.repositories import buscar_alertas_recentes, contar_riscos


router = APIRouter()



@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    
    db = SessionLocal()
    contagem = contar_riscos(db)
    alertas = buscar_alertas_recentes(db)
    db.close()


    if not alertas:
        alertas_html = "<p class='ok'>Nenhum risco crítico no momento.</p>"
    else:
        alertas_html = "".join(
            f"""
            <div class="alert-item">
                <strong>Item {a.sku}</strong>
                <span>Risco {a.risco:.2f}</span>
                <small>{a.criado_em.strftime('%H:%M:%S')}</small>
            </div>
            """
            for a in alertas
        )

    return """
<!DOCTYPE html>
<html>
<head>

  <title>Estoque Vivo</title>
  <style>
    body {
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: #f2f4f8;
      color: #333;
    }

    .header {
      background: linear-gradient(90deg, #1e3c72, #2a5298);
      color: white;
      padding: 20px 30px;
      font-size: 22px;
      font-weight: 600;
    }

    .container {
      padding: 24px 30px;
    }

    .kpis {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }

    .kpi {
      background: white;
      border-radius: 8px;
      padding: 16px;
      box-shadow: 0 2px 6px rgba(0,0,0,.08);
    }

    .kpi span {
      font-size: 13px;
      color: #666;
    }

    .kpi strong {
      font-size: 26px;
      display: block;
      margin-top: 6px;
    }

    .content {
      display: grid;
      grid-template-columns: 2fr 3fr;
      gap: 20px;
      margin-bottom: 24px;
    }

    .card {
      background: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,.08);
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #eee;
    }

    th {
      font-size: 13px;
      color: #555;
    }

    .risk-high {
      background: #d32f2f;
      color: white;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 12px;
    }

    .actions {
      display: flex;
      gap: 12px;
    }

    .btn {
      padding: 10px 14px;
      border-radius: 6px;
      border: none;
      cursor: pointer;
      font-weight: 600;
    }

    .btn-primary {
      background: #2e7d32;
      color: white;
    }

    .btn-secondary {
      background: #1565c0;
      color: white;
    }
  </style>
</head>

<body>

  <div class="header">
    Antecipação de Riscos de Ruptura de Estoque
  </div>

  <div class="container">

    <!-- KPIs -->
    <div class="kpis">
      <div class="kpi"><span>Alertas de Risco</span><strong>5</strong></div>
      <div class="kpi"><span>Itens de Estoque Monitorados</span><strong>25</strong></div>
      <div class="kpi"><span>Pedidos Pendentes</span><strong>78</strong></div>
      <div class="kpi"><span>Previsão de baixa de estoque</span><strong>3 dias</strong></div>
    </div>

    <!-- Conteúdo principal -->
    <div class="content">

      <div class="card">
        <h3>📊 Previsão de Ruptura</h3>
        <p>(Gráfico entra aqui depois)</p>
      </div>

      <div class="card">
        <h3>🚨 Riscos Prioritários</h3>
        <table>
          <tr>
            <th>Item de Estoque</th>
            <th>Produto</th>
            <th>Risco</th>
            <th>Ação</th>
          </tr>
          <tr>
            <td>20</td>
            <td>Fone de Ouvido ELG EP12BK com Fio e Microfone Preto</td>
            <td><span class="risk-high">ALTO • Ação imediata</span></td>
            <td><button class="btn btn-secondary">Detalhes</button></td>
          </tr>
        </table>
      </div>

    </div>

    <!-- Ações -->
    <div class="card">
      <h3>⚙️ Sugestões de Ação</h3>
      <div class="actions">
      <a href="/acoes/aumentar-pedido?item=20" class="btn green">Aumentar Pedido</a>
        <button class="btn btn-secondary">Realocar Estoque</button>
        <button class="btn btn-secondary">Negociar com Fornecedor</button>
      </div>
    </div>

  </div>

</body>
</html>
"""


db = SessionLocal()
contagem = contar_riscos(db)
alertas = buscar_alertas_recentes(db)
db.close()

