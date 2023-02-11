# Create a class called 'Invoice' that a bakery uses to represent an invoice
# for items sold. We assume this bakery takes large orders of one specific item only.
# Ex.: an order of 50 baguettes.
# An Invoice should include the following information: item type, quantity of item,
# price per item and the date the order should be delivered.

class Person:
    """
    this is a class template for a person

    """
    # constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age+=1

person1 = Person("Hannah",20)


print(person1.age)
person1.birthday()
print(person1.age)
print(person1.__doc__)



#this can be improved

class Person: # class always starts with capital letter

    """
    this is a class template for a person
    """
    # constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age+=1

    def __str__(self):
       return self.name + " is " + str(self.age) + " years old"

person1 = Person("Hannah",20)
person2 = Person("Mirka", 30)
print(person1)
print(person2)


