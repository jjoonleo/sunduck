class ClassName:
    static_value = 0

    def __init__(self, attribute):
        self.attribute = attribute
        self.__private_attribute = 0

    def method_name(self):
        print(self.attribute)

    @property
    def property_name(self):
        return self.__private_attribute


my_class = ClassName('attribute')
my_class2 = ClassName('attribute2')
my_class3 = ClassName('attribute2')
my_class4 = ClassName('attribute2')

print(my_class.attribute)
print(my_class2.attribute)


my_class.method_name()
my_class2.method_name()


print(my_class.static_value)
print(my_class2.static_value)
# print(my_class.__dict__)
# my_class.static_value = 1
# print(my_class.__dict__)
