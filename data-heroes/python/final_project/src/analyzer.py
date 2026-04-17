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
        out = {}
        out["total_units"] = int(self.df["units"].sum())
        out["total_revenue"] = int(self.df["revenue"].sum())
        out["average_price"] = float(self.df["price"].mean())
        out["distinct_products"] = int(self.df["product_name"].nunique())
        out["distinct_customers"] = int(self.df["customer_id"].nunique())
        return out
    
    def by_product(self):
        agg = (
            self.df.groupby("product_name", as_index=False)
                .agg(units=("units", "sum"), revenue=("revenue", "sum"))
                .sort_values("revenue", ascending=False)
        )
        return agg
    
    def by_region(self):
        agg = (
            self.df.groupby("region", as_index=False)
                .agg(units=("units", "sum"), revenue=("revenue", "sum"))
                .sort_values("revenue", ascending=False)
        )
        return agg
    
    def by_month(self):
        df = self.df.copy()
        df["year_month"] = df["date"].dt.to_period("M").astype(str)
        agg = (
            df.groupby("year_month", as_index=False)
                .agg(units=("units", "sum"), revenue=("revenue", "sum"))
                .sort_values("year_month")
        )
        return agg
