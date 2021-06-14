class SomeClass(object):
    astr = 34

    def method1(self, number):
        return number * 2


obj = SomeClass()
print(obj.method1(5))
print(obj.astr)
print(SomeClass.__dict__)
