from pathlib import Path
from datetime import date, timedelta
import random
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw"
OUT.mkdir(parents=True, exist_ok=True)
random.seed(7)

rows = []
base = date(2026, 9, 1)
for customer_id in range(1, 301):
    profile = random.choice(["vip", "regular", "new", "risk"])
    if profile == "vip":
        n, max_age, value = random.randint(20, 45), 60, (250, 1200)
    elif profile == "regular":
        n, max_age, value = random.randint(8, 20), 150, (80, 500)
    elif profile == "new":
        n, max_age, value = random.randint(1, 5), 35, (50, 350)
    else:
        n, max_age, value = random.randint(2, 10), 420, (40, 300)
    for _ in range(n):
        rows.append({
            "customer_id": customer_id,
            "purchase_date": (base - timedelta(days=random.randint(0, max_age))).isoformat(),
            "amount": round(random.uniform(*value), 2),
            "category": random.choice(["Tech", "Casa", "Moda", "Esporte"])
        })
pd.DataFrame(rows).to_csv(OUT / "transactions.csv", index=False)
print(f"Geradas {len(rows)} transações.")
