sales = {"laptop": 15, "phone": 25, "headphones": 40}

for i in sales:
    print(i)
    print(sales[i])

for val in sales.values():
    print(val)

for pair in sales.items():
    key, value = pair
    print(f"[PAIR] key: {key}, value: {value}")

for key, value in sales.items():
    print(f"key: {key}, value: {value}")

# znajdz 1szy produkt mający ponad 20szt
for key, value in sales.items():
    if value > 20:
        print(key)
        break
    print("inside for")
print("oustide for")

# pokaz profukty, ktore sprzedaly mniej niz 30szt
for key, value in sales.items():
    if value >= 30:
        print("before continue")
        continue
        print("after continue")
    print(key)
