# 8.3.1
num_1 = 4
num_2 = 0

if num_2 == 0:
    print("can't divide by 0")
elif num_2 < 0:
    print("watch out, you divide by negative number")
    print(num_1 / num_2)
else:
    print(num_1 / num_2)

print(isinstance(num_2, int))
