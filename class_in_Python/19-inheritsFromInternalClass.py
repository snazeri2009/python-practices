class Text(str):
    def Duplicate(self):
        return self + ' ' + self


class Tlist(list):
    def append(self, object):
        print('append in Tlist class')
        super().append(object)
        print('append in List class')


myText = Text("soheila")
print(myText.Duplicate())

myList = Tlist()
print(myList.append("soheila"))
