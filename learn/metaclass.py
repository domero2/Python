class Type:
    pass

Test = type('Test',(),{})

#Creation of the method above are correct

class ToInherite:
    def show(self):
        print('hi mean')

def attribute(f):
    f.z = 9

DownInh = type('DownInh',(ToInherite,),{"x":5, "atr":attribute})

obj1 = DownInh()
obj1.mk = 'cos'
print(obj1.mk)
obj1.show()
obj1.atr()
print(obj1.z)

class Meta(type):
    #create before init method
    def __new__(typself,class_name,bases, attributes):
        print(attributes)

        newDict = {}
        for item, value in attributes.items():
            if item.startswith('__'):
                newDict[item] = value
            else:
                newDict[item.upper()] = value

        print(newDict)
        return type(class_name, bases, newDict)

class NewC(metaclass=Meta):
    x=5
    y=8

    def hello_met(self):
        print("hi something")

inst = NewC()
print(inst.X)

