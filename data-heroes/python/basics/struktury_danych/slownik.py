# 8.4.3
# dictionary -> słownik
# key -> velue

first_dict = {"car": 2000, 1: 2}
first_dict[1]

sales = {
    "coffee": 170
    , "tea": 200
    , "water": 250
}

sales["juice"] = 120
sales["juice"] -= 10

print(sales.keys(), sales.values(), sales.items())
print(sum(sales.values()), sales.get("cola", "not such drink"))

sales.setdefault("fanta", 0)
print(sales)
