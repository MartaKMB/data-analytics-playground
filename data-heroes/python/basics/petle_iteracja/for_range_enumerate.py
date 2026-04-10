products = ["laptop", "phone", "headphone"]
for p in products:
    print(f"- {p}")

pair = ("store", "Warsaw")
for word in pair:
    print(word)

int_list = [3, 5, 7, 9, 12]
for number in int_list:
    print(number*2)
print(int_list)

# print(list(range(4)))

list_len = len(int_list)

for i in range(list_len):
    int_list[i] *= 2

print(int_list)

for idx, price in enumerate(int_list):
    print(f"idx: {idx}, price {price}")
    int_list[idx] *=2

print(int_list)
