import pandas as pd


# Series

s = pd.Series([10,20,30,40])

# print([10,20,30,40])
print(s)
# print(type(s))

# s *= 2
# print(s+20)
# print(s>35)


# DataFrame

data = {
    "product": ["Coffee", "Tea", "Water"],
    "price": [12, 8, 3],
    "units": [120, 80, 200]
}

df = pd.DataFrame(data)

print(df)
# print(type(df))

# df.to_csv("sales.csv", index=False)

# df_csv = pd.read_csv("sales_data.csv")
# print(df_csv.head())
# print(df_csv.tail())

# print(df_csv.info())
# print(df_csv.describe())

# print(df_csv["units"] + 20)
# print(df_csv[["product", "price"]])
# print(df_csv["price"] * df_csv["units"])
