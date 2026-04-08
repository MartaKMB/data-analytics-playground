# 8.4.2
# tuple - krotki

int_tuple = (1,2,3,4)
print(int_tuple)

l1 = [11,12,13]

mix_tuple = (112, "Car", 29.99, l1)
print(mix_tuple[1])
mix_tuple[3][1] = 22
print(mix_tuple)

len(mix_tuple)

mix_tuple.count("Car")
mix_tuple.index("Car")

max(int_tuple)
min(int_tuple)
sum(int_tuple)

base_tuple = (-1,2,3,4,1)

searhed_value = int(input("Number: "))

if searhed_value in base_tuple:
    print(base_tuple.index(searhed_value))
else:
    print("nu such value")
