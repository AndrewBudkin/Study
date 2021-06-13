class SomeClass(object):
    pass


@staticmethod
def squareMethod(x):
    return x * x


print(SomeClass.__dict__)
SomeClass.square = squareMethod
obj = SomeClass()
print(obj.square(5))
print(SomeClass.__dict__)
print(SomeClass.square(5))
