num_1 = input("Number 1: ")
num_2 = input("Number 2: ")
sign = input("Sign [+, -. *, /]: ")

num_1 = float(num_1)
num_2 = float(num_2)

result = 0
valid = True

if sign == "+":
    result = num_1 + num_2
elif sign == "-":
    result = num_1 - num_2
elif sign == "*":
    result = num_1 * num_2
elif sign == "/":
    result = num_1 / num_2
else:
    result_message = "wrong sign!"
    valid = False

if valid:
    result_message = f"Result of {num_1} {sign} {num_2} = {result}"

print(result_message)
