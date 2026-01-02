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
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <title>Antecipação de Riscos de Ruptura</title>

  <style>
    body {
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: #f4f6f8;
      color: #1f2937;
    }

    /* HEADER */
    .header {
      background: linear-gradient(90deg, #1e3a8a, #2563eb);
      color: white;
      padding: 20px 30px;
      font-size: 22px;
      font-weight: 600;
    }

    .container {
      padding: 30px;
    }

    /* KPI CARDS */
    .kpis {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 30px;
    }

    .kpi {
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    .kpi span {
      font-size: 14px;
      color: #6b7280;
    }

    .kpi strong {
      display: block;
      font-size: 28px;
      margin-top: 5px;
    }

    /* GRID PRINCIPAL */
    .main-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 20px;
      margin-bottom: 30px;
    }

    .card {
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    .card h3 {
      margin-top: 0;
      margin-bottom: 15px;
      font-size: 18px;
    }

    /* TABELA */
    table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      padding: 12px;
      border-bottom: 1px solid #e5e7eb;
      text-align: left;
    }

    th {
      color: #6b7280;
      font-size: 13px;
      text-transform: uppercase;
    }

    .badge {
      padding: 6px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: bold;
      color: white;
    }

    .alto {
      background: #dc2626;
    }

    .btn {
      padding: 8px 14px;
      border-radius: 6px;
      background: #2563eb;
      color: white;
      text-decoration: none;
      font-size: 14px;
    }

    /* AÇÕES */
    .actions {
      display: flex;
      gap: 15px;
      margin-bottom: 30px;
    }

    .action-btn {
      padding: 12px 18px;
      border-radius: 8px;
      color: white;
      text-decoration: none;
      font-weight: 500;
    }

    .green { background: #16a34a; }
    .blue { background: #2563eb; }

    /* INDICADORES */
    .indicators {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }

    .indicator {
      background: white;
      padding: 20px;
      border-radius: 10px;
      text-align: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    .indicator strong {
      font-size: 26px;
      display: block;
      margin-top: 8px;
    }

    .causas-acoes {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 30px;
}

.causas-lista {
  list-style: none;
  padding: 0;
  margin: 0;
}

.causas-lista li {
  padding: 12px 0;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  gap: 10px;
}

.causas-lista li:last-child {
  border-bottom: none;
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
      <div class="kpi"><span>Alertas de Risco</span><strong>15</strong></div>
      <div class="kpi"><span>Itens Monitorados</span><strong>320</strong></div>
      <div class="kpi"><span>Pedidos Pendentes</span><strong>78</strong></div>
      <div class="kpi"><span>Previsão de Ruptura</span><strong>9 dias</strong></div>
    </div>

    <!-- GRID PRINCIPAL -->
    <div class="main-grid">

      <div class="card">
        <h3>📊 Gráfico de Previsão de Ruptura</h3>
        <p>(Gráfico entra aqui depois)</p>
      </div>

      <div class="card">
        <h3>🚨 Riscos Prioritários</h3>

        <table>
          <thead>
            <tr>
              <th>Item</th>
              <th>Produto</th>
              <th>Risco</th>
              <th>Ação</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>20</td>
              <td>Fone de Ouvido ELG EP12BK</td>
              <td><span class="badge alto">ALTO</span></td>
              <td><a class="btn" href="#">Ver Detalhes</a></td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>

   <div class="causas-acoes">
<div class="card" style="margin-bottom: 30px;">
  <h3>🧠 Análise de Causas Prováveis</h3>

  <ul class="causas-lista">
    <li style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #e5e7eb;">
      📈 <span>Demanda acima do esperado</span>
    </li>
    <li style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #e5e7eb;">
      🚚 <span>Atraso no fornecimento</span>
    </li>
    <li style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid #e5e7eb;">
      🔄 <span>Falha no reabastecimento</span>
    </li>
    <li style="display:flex;align-items:center;gap:10px;padding:10px 0;">
      ⚠️ <span>Problemas logísticos</span>
    </li>
  </ul>
</div>


    
    <div class="card">

      <h3>⚙️ Sugestões de Ação</h3>
      <div class="actions">
        <a class="action-btn green" href="#">Aumentar Pedido</a>
        <a class="action-btn blue" href="#">Realocar Estoque</a>
        <a class="action-btn blue" href="#">Negociar com Fornecedor</a>
      </div>
    </div>
    </div>


    <!-- INDICADORES -->
    <div class="indicators">
      <div class="indicator"><span>Cobertura de Estoque</span><strong>4 dias</strong></div>
      <div class="indicator"><span>Nível de Serviço</span><strong>92%</strong></div>
      <div class="indicator"><span>Pedidos Atrasados</span><strong>23</strong></div>
      <div class="indicator"><span>ROF</span><strong>34%</strong></div>
    </div>

  </div>

</body>
</html>
"""

db = SessionLocal()
contagem = contar_riscos(db)
alertas = buscar_alertas_recentes(db)
db.close()

