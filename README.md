# Customer Intelligence

Projeto de **segmentação de clientes** que combina SQL, análise RFM e Machine Learning (K-Means). A solução transforma transações em atributos comportamentais e classifica clientes em grupos úteis para ações de CRM.

## Stack
Python, Pandas, SQLite, SQL, scikit-learn

## Execução
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

## Testes
```bash
python -m unittest discover -s tests -v
```
