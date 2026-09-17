import sys
from pathlib import Path
import unittest
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.segment import segment_customers

class TestSegmentation(unittest.TestCase):
    def test_all_rows_receive_segment(self):
        df = pd.DataFrame({
            "customer_id": range(1,9),
            "recency": [1,2,20,25,70,80,200,250],
            "frequency": [30,25,15,14,6,5,2,1],
            "monetary": [9000,8000,4000,3500,1000,900,200,100],
            "avg_ticket": [300,320,260,250,160,180,100,100],
        })
        out = segment_customers(df, 4)
        self.assertEqual(out["segment"].isna().sum(), 0)
        self.assertEqual(len(set(out["segment"])), 4)

if __name__ == "__main__": unittest.main()
