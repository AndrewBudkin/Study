class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'


my_laptop = Laptop('hp', '15-bw0xx', '17 000')
print(my_laptop.laptop_name)
laptop1 = Laptop('Apple', 'MacBook', 60000)
laptop2 = Laptop('Lenovo', "IdeaPad", 15000)
