# public attr and methods / Обычные атрибуты и методы, которые можно вызывать вне класса
class BankAccountPublic():
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data_public(self):
        print(self.name, self.balance, self.passport, sep=', ')


# protected attr and methods / Его можно вызвать вне класса, но делать это не рекомендуется
class BankAccountProtected():
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_data_protected(self):
        print(self._name, self._balance, self._passport, sep=', ')


# private attr and methods / Его можно вызвать вне класса, но делать это не рекомендуется
class BankAccountPrivate():
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data_private(self):
        print(self.__name, self.__balance, self.__passport, sep=', ')


account1 = BankAccount('Bob', 17000, 13556434675)
account1.print_data()
