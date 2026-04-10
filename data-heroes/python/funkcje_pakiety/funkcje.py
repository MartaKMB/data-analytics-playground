def print_numbers(min_number, max_number):
    for num in range(min_number, max_number):
        print(num)

print_numbers(2, 5)
print_numbers(max_number = 7, min_number = 4)

def net_privce(gross, vat_rate):
    return gross / (1 + vat_rate)

def net_privce_with_default(gross, vat_rate = 0.23):
    return gross / (1 + vat_rate)


net = net_privce(10, 0.23)
net2 = net_privce(20, 0.19)
net3 = net_privce_with_default(10)
print(net, net3, net2)
