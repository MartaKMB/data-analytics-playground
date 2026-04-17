import os
import pandas as pd

class DataFileNotFoundError(Exception):
    pass

class InvalidSchematError(Exception):
    pass

class Loader:
    def __init__(self, data_dir="../data"):
        self.data_dir = data_dir

        self.path_products = os.path.join(self.data_dir, "products.csv")
        self.path_customers = os.path.join(self.data_dir, "customers.csv")
        self.path_sales = os.path.join(self.data_dir, "sales.csv")

    def _ensure_exists(self, path):
        if not os.path.exists(path):
            raise DataFileNotFoundError(f"Expected file not found: {path}")
        
    def _read_csv(self, path):
        try:
            df = pd.read_csv(path)
            return df
        except FileNotFoundError:
            raise DataFileNotFoundError(f"File not found: {path}")
        except pd.errors.EmptyDataError:
            raise InvalidSchematError(f"File is empty or has no rows: {path}")
        except pd.errors.ParserError as e:
            raise InvalidSchematError(f"CSV parse error in {path}: {e}")
        
    def _validate_columns(self, df, required_cols, file_label):
        missing = []
        for column in required_cols:
            if column not in df.columns:
                missing.append(column)
        if missing:
            raise InvalidSchematError(
                f"Missing required columns in {file_label}: {missing}\n"
                f"Found coulmns: {list(df.columns)}"
            )

    def load_products(self):
        self._ensure_exists(self.path_products)
        df = self._read_csv(self.path_products)
        self._validate_columns(df, ["product_id", "product_name", "category", "price"], "products.csv")
        return df
    
    def load_customers(self):
        self._ensure_exists(self.path_customers)
        df = self._read_csv(self.path_customers)
        self._validate_columns(df, ["customer_id", "customer_name", "region", "age"], "customers.csv")
        return df
    
    def load_sales(self):
        self._ensure_exists(self.path_sales)
        df= self._read_csv(self.path_sales)
        self._validate_columns(df, ["sale_id", "product_id", "customer_id", "units", "date"], "sales.csv")
        return df

    def load_all(self):
        products = self.load_products()
        customers = self.load_customers()
        sales = self.load_sales()
        return products, customers, sales
