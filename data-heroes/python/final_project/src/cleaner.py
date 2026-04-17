import pandas as pd

class Cleaner:
    def __init__(self):
        pass

    def _standarize_columns(self, df):
        df = df.copy()
        new_cols = []
        for column in df.columns:
            clean_name = column.strip().lower()
            new_cols.append(clean_name)
        df.columns = new_cols
        return df
    
    def _drop_duplicate(self, df, subset=None):
        before = len(df)
        df = df.drop_duplicates(subset=subset)
        after = len(df)
        print(f"Dropped duplicates: {before} : {after}")
        return df
    
    def clean_products(self, df_products):
        df = self._standarize_columns(df_products)
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df = df[df["price"].notna()]
        df = df[df["price"] > 0]
        df = self._drop_duplicate(df, subset=["product_id"])
        return df
    
    def clean_customers(self, df_customers):
        df = self._standarize_columns(df_customers)
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
        median_age = df["age"].median()
        df["age"] = df["age"].fillna(median_age)
        df = self._drop_duplicate(df, subset=["customer_id"])
        return df
    
    def clean_sales(self, df_sales):
        df = self._standarize_columns(df_sales)
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["units"] = pd.to_numeric(df["units"], errors="coerce")
        df["units"] = df["units"].fillna(0)
        df = df[df["units"] >= 0]
        df = df[df["date"].notna()]
        df = self._drop_duplicate(df, subset=["sale_id"])
        return df

    def enrich_sales_with_dimensions(self, df_sales, df_products, df_customers):
        merged = df_sales.merge(
            df_products[["product_id", "product_name", "category", "price"]],
            on="product_id",
            how="left"
        )
        merged = merged.merge(
            df_customers[["customer_id", "customer_name", "region", "age"]],
            on="customer_id",
            how="left"
        )
        merged = merged.dropna(subset=["product_name", "customer_name"])
        return merged
