product_dic = {"name" : "laptop", "net_price" : 3200.0, "vat_rate" : 0.23}

def gross_price(net_price, vat_rate):
    return net_price * (1 + vat_rate)

print(f"GROSS (dict + function): {gross_price(product_dic["net_price"], product_dic["vat_rate"])}")

class Product:
    def __init__(self, name, net_price, vat_rate):
        self.name = name
        self.net_price = net_price
        self.vat_rate = vat_rate
    
    def gross_price(self):
        return self.net_price * (1 + self.vat_rate)
    
laptop = Product("laptop", 3200.0, 0.23)
phone = Product("phone", 1450.0, 0.23)

print(f"GROSS class: {laptop.gross_price()}")
