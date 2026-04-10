class Product:
    product_count = 0

    def __init__(self, name, net_price, vat_rate):
        self.name = name
        self.net_price = net_price
        self.vat_rate = vat_rate
        Product.product_count += 1
    
    def gross_price(self):
        return self.net_price * (1 + self.vat_rate)
    
    def apply_discount(self, discount = 10):
        self.net_price = self.net_price * (1 - discount)

    def __str__(self):
        return f"Product (name= '{self.name}', net= {self.net_price}, VAT= {self.vat_rate}, gross= {round(self.gross_price(), 2)})"
    
laptop = Product("laptop", 3200.0, 0.23)

# nadpisywanie mozliwe ale zla praktyka
# laptop.net_price *= 0.9
# print(laptop.net_price)

laptop.apply_discount(0.2)
print(laptop.net_price)

print(Product.product_count)
phone = Product("phone", 1450.0, 0.23)
print(Product.product_count)

print(laptop)
