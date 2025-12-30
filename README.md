# 📦 Estoque Vivo – MVP de Monitoramento de Ruptura no Varejo

O **Estoque Vivo** é um MVP de software desenvolvido para **antecipar riscos de ruptura de estoque** no varejo, utilizando dados operacionais simples (vendas e estoque) para gerar **alertas automáticos e históricos de risco**.

O objetivo é apoiar times de operação e supply chain com **informações acionáveis**, indo além do estoque estático de ERPs tradicionais.

---

## 🚀 Principais Funcionalidades

- 📊 Cálculo automático de risco de ruptura
- 🔁 Job periódico de monitoramento
- 🚨 Alertas automáticos por e-mail em caso de risco alto
- 💾 Persistência de histórico em banco SQLite
- 🔍 API para consulta de histórico por SKU
- 🖥️ Dashboard simples e visual para acompanhamento
- 📄 Documentação automática via Swagger (OpenAPI)

---

## 🧠 Conceito Central

Em vez de tratar estoque como um número fixo, o sistema trabalha com **probabilidade de ruptura**, considerando o comportamento real de vendas.

Classificação de risco:
- **BAIXO (0.0 – 0.4)** → Operação normal
- **MÉDIO (0.5 – 0.7)** → Atenção / monitorar
- **ALTO (0.8 – 1.0)** → Ação imediata
