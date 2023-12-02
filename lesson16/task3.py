class Product:

    def __init__(self, type_ : str, name : str, price : float):
        self.type_ = type_
        self.name = name
        self.price = price

class ProductStore:
    
    products = []
    income = 0

    def add(self, product, amount : int):
        self.products.append(dict(type_=product.type_, name=product.name, price=product.price * 1.3, amount=amount))
    
    def set_discount(self, identifier : str, percent : int, identifier_type="type_"):
        for product in self.products:
            if product[identifier_type] == identifier:
                product["price"] *= (100 - percent) / 100
    
    def sell_product(self, product_name : str, amount : int):
        for product in self.products:
            if product["name"] == product_name:
                if product["amount"] >= amount:
                    product["amount"] -= amount
                    self.income += amount * product["price"]
                else:
                    print("Обраного продукту нема в наявності")
    
    def get_income(self):
        return self.income
    
    def get_all_products(self):
        return self.products
    
    def get_product_info(self, product_name : str):
        for product in self.products:
            if product["name"] == product_name:
                return tuple([product["name"], product["amount"]])

p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product("Ramen", 10)
assert s.get_product_info("Ramen") == ("Ramen", 290)