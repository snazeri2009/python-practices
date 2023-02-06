# this code create a personal data structure and you can use ans redefine your magic methods
# and can set and get item
# user may be enter soheila Soheila SOHEILA ,... and you want to set only one key for this string
# you can user .lower or .upper to get small or large string to set
class myDataStructures:
    # create a list empty data structure
    def __init__(self):
        # if you want to Inaccessible from outside the class, you can set __ before structure
        # private data structure  with __ before structure
        self.__data = {}

    # add count to data structure
    # if key is not with get you can add key to data structure
    def add(self,  key):
        self.__data[key.lower()] = self.__data.get(key.lower(), 0) + 1

    # get count from data structure .this is a instance method
    def get(self, key):
        return self.__data.get(key.lower(), 0)
    # this is a magic method

    def __getitem__(self, key):
        return self.__data.get(key.lower(), 0)

    # this is a magic method
    def __setitem__(self, key, count):
        self.__data[key.lower()] = count

    # this is a magic method
    def __len__(self):
        return len(self.__data)

    # this is a magic method
    def __iter__(self):
        return iter(self.__data)


myStructure1 = myDataStructures()
myStructure1.add("soheila")
myStructure1.add("SOHEILA")
myStructure1.add("SoHeila")
myStructure1.add("sohEILA")
myStructure1.add("sara")
myStructure1.add("SARA")
myStructure1.add("SAra")
print('========================')
print(myStructure1.get("soheila"))  # instance method for   myStructure
print(myStructure1.__getitem__("soheila"))  # magic method for   myStructure


myStructure1["sohEILA"] = 20
myStructure1["sima"] = 15
print('========================')
print(myStructure1.get("soheila"))  # instance method for   myStructure
print(myStructure1.__getitem__("sima"))  # magic method for   myStructure
print('========================')
print(len(myStructure1))
print('========================')
# with __ in data in class you can not accessible to data
for i in myStructure1.data:
    print(i)
print('========================')
