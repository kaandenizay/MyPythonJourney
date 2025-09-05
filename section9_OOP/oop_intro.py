
# a = 12
# b = 4
# print(a + b)
# print(a.__add__(b))


class Kettle:

    power_source = "electricity" # class attribute, shared by instances
    # Similar to static fields in Java, but not exactly same

    def __init__(self, make, price):
        self.make = make # make is attribute
        self.price = price # price is another attribute
        self.on = False # on is also attribute

    def switch_on(self):
        self.on = True

kenwood = Kettle('Kenwood', 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle('Hamilton', 14.99)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
Constructor (init method): Refers to a special method that is executed when an instance of a class is created
"""

print(hamilton.on)
hamilton.switch_on() # here we are calling via instance, there is no need to pass argument
print(hamilton.on)

Kettle.switch_on(kenwood) # here we are calling on class, we need to pass argument as instance
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

"""
Python classes are dynamic and it can be modified after their created
"""
kenwood.power = 1.5
print (kenwood.power)
# print(hamilton.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)