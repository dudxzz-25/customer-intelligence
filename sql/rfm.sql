-- reference_date is fixed to keep the project reproducible.
WITH base AS (
  SELECT
    customer_id,
    CAST(julianday('2026-09-16') - julianday(MAX(purchase_date)) AS INTEGER) AS recency,
    COUNT(*) AS frequency,
    ROUND(SUM(amount), 2) AS monetary,
    ROUND(AVG(amount), 2) AS avg_ticket
  FROM transactions
  GROUP BY customer_id
)
SELECT * FROM base ORDER BY customer_id;
