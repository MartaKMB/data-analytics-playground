products = ["laptop", "phone", "headphones"]

laptop_data = (1, "laptop", 3200.00)
phone_data = (2, "phone", 2100.00)
headphones_data = (3, "headphones", 550.00)

sales = {
   "laptop": 15
   , "phone": 25
   , "headphones": 40 
}

print("PRODUCTS")
print(products)

total_units = sum(sales.values())
print(f"Total units sold: {total_units}")

laptop_revenue = sales["laptop"] * laptop_data[2]
phone_revenue = sales["phone"] * phone_data[2]
headphones_revenue = sales["headphones"] * headphones_data[2]
total_revenue = laptop_revenue + phone_revenue + headphones_revenue
print(f"Total revenue: {total_revenue}")
