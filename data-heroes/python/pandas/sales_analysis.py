import pandas as pd

# GROUP BY
print("- - - GROUPBY - - -")

sales_data ={
    "product": ["Coffee", "Tea", "Water", "Coffee", "Tea", "Water"],
    "region": ["North", "North", "North", "South", "North", "South"],
    "units": [120, 80, 200, 150, 100, 250],
    "price": [12, 8, 3, 12, 8, 3]
}

sales = pd.DataFrame(sales_data)

print(sales.groupby("product")["units"].sum())
# print(sales.groupby(["product", "region"])["units"].agg(["sum", "mean"]))

# JOIN
print("- - - MERGE | CONCAT - - -")

products = pd.DataFrame({
    "product": ["Coffee", "Tea", "Water", "Juice"],
    "category": ["Hot", "Hot", "Cold", "Cold"]
})

sales_summary = pd.DataFrame({
    "product": ["Coffee", "Tea", "Water"],
    "total_units": [270, 180, 450]
})

merged = pd.merge(products, sales_summary, how = "left", on = "product")
# merged = pd.merge(products, sales_summary, how = "inner", on = "product")
print(merged)

sales_q1 = sales_summary.copy()
sales_q1["quarter"] = "Q1"
sales_q2 = sales_summary.copy()
sales_q2["quarter"] = "Q2"

concat_df = pd.concat([sales_q1, sales_q2])
print(concat_df)
