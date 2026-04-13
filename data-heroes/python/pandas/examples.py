import pandas as pd

# 8.10.2

# SERIES

s = pd.Series([10,20,30,40])

# print([10,20,30,40])
# print(s)
# print(type(s))

# s *= 2
# print(s+20)
# print(s>35)

# DATA FRAME

data = {
    "product": ["Coffee", "Tea", "Water"],
    "price": [12, 8, 3],
    "units": [120, 80, 200]
}

df = pd.DataFrame(data)

# print(df)
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

# 8.10.3

# LOC, ILOC

data_3 = {
    "product": ["Coffe", "Tea", "Water", "Juice", "Soda"],
    "price": [12, 8, 3, 5, 7],
    "units": [120, 80, 200, 60, 150]
}

df_3 = pd.DataFrame(data_3)
# print(df_3)

# print(df_3.loc[0:2], "price", "units") # po indexie i nazwie rekordu
# print(df_3.loc[0:1])

# print(df_3.iloc[0]) # po kolejności, lokalizacja kratki
# print(df_3.iloc[0:2, 1:3])

# maski boolowe
# print(df_3["units"] > 100)

# print(df_3.loc[df_3["units"] > 100, ["product", "units"]])

df_3_2 = df_3.set_index("product")
# print(df_3_2)
# print(df_3_2.loc["Coffe"])

df_3_reset = df_3_2.reset_index()

# print(df_3_reset)

df_3_custom = pd.DataFrame(data_3, index = ['a', 'b', 'c', 'd', 'e'])

# print(df_3_custom)
# print(df_3_custom.loc['c'])

# 8.10.4

# NAN

data_4 = {
    "product": ["Coffe", "Tea", "Water", "Juice"],
    "price": [12, 8, None, 5],
    "units": [120, None, 200, 80],
    "region": ["North", "South", "East", None]
}

df_4 = pd.DataFrame(data_4)
# print(df_4)
# print(df_4.isna().any()) # isna True and False, so additioal any

# print(df_4.describe())
# print(df_4.dropna());

df_4_filled = df_4.fillna({"price": 10, "units": 0, "region": "Unknown"})
# print(df_4_filled)

# STASTISTICS - COLUMNS

# print(df_4_filled.sum())
# print(df_4_filled.max())
# print(df_4_filled[["price", "units"]].min())

# STATISTICS - RECORDS, ROWS

print(df_4_filled[["price", "units"]].max(axis=1))
