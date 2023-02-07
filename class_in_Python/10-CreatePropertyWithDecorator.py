# In Python programming, a decorator is a special type of function that modifies or
# extends the behavior of another function. It allows you to wrap an existing function with additional code,
# making it reusable and flexible. Decorators are denoted with the @ symbol, followed by the decorator name,
# and placed immediately before the function definition that is to be decorated.


class Product:
    # this is the constructorوmagic Method for the Product class ,we create a magic Method : __name__
    def __init__(self, _price, _name, _count):
        self.price = _price
        self.ProductName = _name
        self.Count = _count
    # ===============================================   properties =================================
    # ===============================================   Name       =================================
    # ProductName property

    @property
    def ProductName(self):   # getter
        return self.__ProductName

    @ProductName.setter
    def ProductName(self, value):
        self.__ProductName = value

    # ===============================================   price  ====================================
    # price property
    @property
    def price(self):    # getter
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("this is not a valid price")
        self.__price = value
    # ===============================================   Count  ====================================
    # count property

    @property
    def Count(self):  # getter
        return self.__CountProduct

    @Count.setter
    def Count(self, value):
        if value < 0:
            raise ValueError("this is not a valid price")
        self.__CountProduct = value
    # =============================================== ================================================


myProduct = Product(_name='kola', _count=10, _price=25000)
print("Name is : ", myProduct.ProductName)
print("Count is : ", myProduct.Count)
print("Price is : ", myProduct.price)
# myProduct.price = 10  # call set_prices(self):
# myProduct.price=-10 #show an error message
