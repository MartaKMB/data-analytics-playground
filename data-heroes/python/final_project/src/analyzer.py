import pandas as pd

class SalesAnalyzer:
    def __init__(self, sales_enriched_df):
        self.df = sales_enriched_df.copy()
        required = ["units", "price", "product_name", "category", "region", "date"]
        missing = []
        for c in required:
            if c not in self.df.columns:
                missing.append(c)
        if missing:
            raise ValueError(f"SalesAnalyzer missing required columns: {missing}")
        self.df = self.df[self.df["date"].notna()]
        self._add_revenue()

    def _add_revenue(self):
        self.df["revenue"] = self.df["units"] * self.df["price"]

    def kpis(self):
        print("KPI")
