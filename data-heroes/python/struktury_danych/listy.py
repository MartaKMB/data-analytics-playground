# 8.4.1
# list

int_list = [11, 24, 55, 1, 2, 3, 54]
print(int_list[1])

str_list = ["apple", "orange", "banana"]
print(str_list[2])

mix_list = [13, 2.7, "car", 256, str_list]
print(mix_list[4][1])

# wycinek listy
print(int_list[0 : 3])
print(int_list[1 : ])
print(int_list[ : 4])

int_list[1] = int_list[1] + 1
print(int_list)

int_list.append(30)
print(int_list)

int_list.remove(11)
print(int_list)

print(len(int_list))
