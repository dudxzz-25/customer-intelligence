from pathlib import Path
import sqlite3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "transactions.csv"
OUT = ROOT / "data" / "output"
DB = OUT / "customer_intelligence.db"
SQL = ROOT / "sql" / "rfm.sql"
OUT.mkdir(parents=True, exist_ok=True)


def load_transactions(csv_path=RAW, db_path=DB):
    df = pd.read_csv(csv_path)
    df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["customer_id", "purchase_date", "amount"])
    df = df[df["amount"] > 0]
    df["purchase_date"] = df["purchase_date"].dt.strftime("%Y-%m-%d")
    with sqlite3.connect(db_path) as conn:
        df.to_sql("transactions", conn, if_exists="replace", index=False)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_tx_customer ON transactions(customer_id)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_tx_date ON transactions(purchase_date)")
    return df


def calculate_rfm(db_path=DB):
    query = SQL.read_text(encoding="utf-8")
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(query, conn)


def segment_customers(rfm: pd.DataFrame, n_clusters=4):
    features = ["recency", "frequency", "monetary", "avg_ticket"]
    scaler = StandardScaler()
    X = scaler.fit_transform(rfm[features])
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=20)
    result = rfm.copy()
    result["cluster"] = model.fit_predict(X)

    # Human-readable labels are derived from cluster centroids, not hard-coded cluster IDs.
    summary = result.groupby("cluster").agg(
        recency=("recency", "mean"), frequency=("frequency", "mean"), monetary=("monetary", "mean")
    )
    score = (-summary["recency"].rank() + summary["frequency"].rank() + summary["monetary"].rank())
    ordered = list(score.sort_values(ascending=False).index)
    names = ["VIP", "Recorrente", "Potencial", "Em risco"]
    mapping = {cluster: names[i] for i, cluster in enumerate(ordered)}
    result["segment"] = result["cluster"].map(mapping)
    return result


def main():
    load_transactions()
    rfm = calculate_rfm()
    segmented = segment_customers(rfm)
    segmented.to_csv(OUT / "customer_segments.csv", index=False)
    summary = segmented.groupby("segment").agg(
        customers=("customer_id", "count"),
        avg_recency=("recency", "mean"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
    ).round(2)
    summary.to_csv(OUT / "segment_summary.csv")
    print(summary)

if __name__ == "__main__":
    main()
