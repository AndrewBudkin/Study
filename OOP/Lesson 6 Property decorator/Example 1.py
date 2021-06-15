class Money:
    def __init__(self, dollars, cents):
        self.__dollars = dollars
        self.__cents = cents
        self.__total_cents = dollars, cents

    @property
    def dollars(self):
        return self.__dollars



d = Money(90, 56)
d.dollars