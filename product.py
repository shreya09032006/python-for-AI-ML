class product:

    count = 0
    def __init__(self, name , price):
        self.name=name
        self.price=price
        product.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = { price - (price * discount / 100)}")

p1 = product("iphone" , 900000)
p2 = product("macbook" , 700000)       

p1.get_info()
p2.get_info()
p1.calc_discount(10000 , 36)