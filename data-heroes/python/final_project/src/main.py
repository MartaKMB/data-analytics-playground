from loader import Loader
# from cleaner import Cleaner
# from analyzer import SalesAnalyzer
# import visualizer as viz
import os

print(os.getcwd())
loader = Loader(data_dir="data-heroes/python/final_project/data")

try:
    products, customers, sales = loader.load_all()
except Exception as e:
    print("Data loading error: ", e)
    raise SystemExit(1)
