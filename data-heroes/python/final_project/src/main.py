from loader import Loader
from cleaner import Cleaner
from analyzer import SalesAnalyzer
# import visualizer as viz
import os

print(os.getcwd())
loader = Loader(data_dir="data-heroes/python/final_project/data")

try:
    products, customers, sales = loader.load_all()
except Exception as e:
    print("Data loading error: ", e)
    raise SystemExit(1)

cleaner = Cleaner()
products = cleaner.clean_products(products)
customers = cleaner.clean_customers(customers)
sales = cleaner.clean_sales(sales)
sales_enriched = cleaner.enrich_sales_with_dimensions(sales, products, customers)

analyzer = SalesAnalyzer(sales_enriched)
kpis = analyzer.kpis()
by_prod = analyzer.by_product()
by_reg = analyzer.by_region()
by_mon = analyzer.by_month()
