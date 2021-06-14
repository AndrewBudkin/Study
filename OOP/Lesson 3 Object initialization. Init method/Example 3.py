class Zebra():
    def __init__(self, count=1):
        self.count = count

    def which_stripe(self):
        self.count += 1
        if self.count % 2 == 0:
            return 'Полоска белая'
        else:
            return 'Полоска черная'


z1 = Zebra()
print(z1.which_stripe())  # печатает "Полоска белая"
print(z1.which_stripe())  # печатает "Полоска черная"
print(z1.which_stripe())
