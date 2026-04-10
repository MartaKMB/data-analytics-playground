sales_data = {
    "laptop": {"units": 15, "price": 1200.00},
    "phone": {"units": 25, "price": 2100.00},
    "headphones": {"units": 40, "price": 550.00}
}

print("Product list")
for product in sales_data:
    print(f"- {product}")

total_units = 0
for data in sales_data.values():
    total_units += data["units"]

print(f"TOTAL UNITS: {total_units}")

total_revenue = 0

for product, data in sales_data.items():
    total_revenue += data["units"] * data["price"]

print(f"TOTAL REVENUE: {total_revenue}")
