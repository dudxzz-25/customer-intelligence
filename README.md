# Customer Intelligence

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-RFM-3776AB?logo=python&logoColor=white">
  <img alt="SQL" src="https://img.shields.io/badge/SQL-Analytics-4479A1">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-KMeans-F7931E?logo=scikitlearn&logoColor=white">
  <a href="https://github.com/dudxzz-25/customer-intelligence/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/dudxzz-25/customer-intelligence/actions/workflows/ci.yml/badge.svg"></a>
</p>


[![CI](https://github.com/dudxzz-25/customer-intelligence/actions/workflows/ci.yml/badge.svg)](https://github.com/dudxzz-25/customer-intelligence/actions/workflows/ci.yml)

Projeto de **segmentação de clientes** que combina SQL, análise RFM e Machine Learning com K-Means. A solução transforma transações em atributos comportamentais e organiza os clientes em grupos úteis para CRM e priorização comercial.

## 🎯 Objetivo

Responder perguntas como:

- quais clientes concentram maior valor?
- quais possuem comportamento recorrente?
- quais demonstram potencial de crescimento?
- quais apresentam sinais de risco de afastamento?

## 🛠️ Stack

**Python · Pandas · SQL · SQLite · scikit-learn · K-Means**

## 🔎 Metodologia

1. geração/carregamento das transações;
2. cálculo de **Recency, Frequency, Monetary e Ticket Médio** em SQL;
3. padronização das variáveis;
4. clusterização com K-Means;
5. ordenação dos clusters por comportamento para gerar rótulos interpretáveis.

A data de referência do RFM é fixa no SQL para manter os resultados reproduzíveis.

## 📊 Resultado atual

| Segmento | Clientes | Recência média | Frequência média | Valor monetário médio |
|---|---:|---:|---:|---:|
| VIP | 69 | 16,54 | 33,39 | 24.439,34 |
| Recorrente | 75 | 23,87 | 14,27 | 4.014,65 |
| Potencial | 132 | 38,02 | 4,70 | 891,85 |
| Em risco | 24 | 186,21 | 4,08 | 728,43 |

> Os dados são sintéticos e os segmentos têm finalidade demonstrativa.

## 📂 Estrutura

```text
customer-intelligence/
├── data/
│   ├── raw/
│   └── output/
├── scripts/generate_data.py
├── sql/rfm.sql
├── src/segment.py
├── tests/test_segment.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_data.py
python src/segment.py
```

Saídas em `data/output/`:

- `customer_segments.csv`
- `segment_summary.csv`
- `customer_intelligence.db`

### Testes

```bash
python -m unittest discover -s tests -v
```

## ⚠️ Limitações

- K-Means pressupõe grupos aproximadamente separáveis no espaço das features;
- os nomes dos segmentos são interpretações dos clusters, não verdades universais;
- comportamento futuro, canal, margem e perfil demográfico não entram no modelo atual.

---

Desenvolvido por **Eduardo de Toledo Dias**.

[Portfólio](https://dudxzz-25.github.io/portfolio-web/) · [GitHub](https://github.com/dudxzz-25) · [LinkedIn](https://www.linkedin.com/in/eduardo-de-toledo-dias-880b9834b/)