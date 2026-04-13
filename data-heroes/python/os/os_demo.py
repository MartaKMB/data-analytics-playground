import os
import pandas as pd
import matplotlib.pyplot as plt

print("Current working directory: ", os.getcwd())
print("Contents: ", os.listdir())

if not os.path.exists("data-heroes/python/os/reports"):
    print("create folder")
    os.makedirs("data-heroes/python/os/reports")
else:
    print("folder already exists")

file_path = "data-heroes/python/os/reports/test.txt"

with open(file_path, "w") as file:
    file.write("Hello text file!")
    print("Created file: ", file_path)

os.chdir("data-heroes/python/os/reports")
print("Current working directory: ", os.getcwd())
print("Contents: ", os.listdir())

df = pd.DataFrame({
    "product": ["Coffee", "Tea", "Water"],
    "units": [120, 80, 200],
    "price": [12, 8, 3]
})

df["revenue"] = df["units"] * df["price"]

df.to_csv("sales.csv", index=False)

df.plot(x="product", y="revenue", kind="bar", title="Revenue per product")
plt.savefig("sales_chart.png")
