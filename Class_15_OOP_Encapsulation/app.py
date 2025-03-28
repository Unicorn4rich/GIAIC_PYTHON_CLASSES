#<-------------------------------------------------------------------------------------->
# encapsulation

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Shoaib(Person):
#     pass



# name1 = Shoaib("ahoaib", 23)

# print(name1.name)



#<-------------------------------------------------------------------------------------->
# Access modifire
# 1. Public
# 2. Protected
# 3. Private


# example 1
class Person():
    def __init__(self):
        self.name = "shoaib"      # Public attribute
        self._last_name = "Ahmed" # Protected
        self.__age = 23           # Private
        
        
    # getter method
    def get_age(self):  # is method se hamne prvate value access hogi.
        return self.__age   
    
    # setter method 
    def set_age(self, age):
        self.__age = age  
        
        
# example 2        
class Employee(Person):
    pass



# emp = Employee()
# print(emp.__age)

# This is: Public
# print(emp.name) # shoaib from parent class => Person()
# emp.name = "azlaan"
# print(emp.name) # azlaan changes.



per = Person()
# # print(per.__age) # access nahi hogi beacause ye => private hai.
# print(per.get_age()) # 23 => is method se hamne prvate value access hui.
# per.set_age(30)      # set value => 30
# print(per.get_age()) # get that set value or priavte method => 30

# print(per._last_name)
# per._last_name = "abc"
# print(per._last_name)

# per.__age = 70       # not set in private
# print(per.get_age())


print(per._Person__age) # now you can get value without gettter method.


emp = Employee()

# print(emp.get_age()) # old value => 23
# emp.set_age(50)      # new set value => 50
# print(emp.get_age()) # get set value => 50

# print(emp._last_name)     # Ahmed
# emp._last_name = "azlaan" # set value
# print(emp._last_name)     # azlaan