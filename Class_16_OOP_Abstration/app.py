# from abc import ABC, abstractmethod # => Abstract Base Class


# Abstraction => ye complexity ko chupata hai user se
# Abstract    => ye blueprint hai jo apni child class par rules apply karta hai 
# Abstract Class => ye apni child class par rules apply karta hai ke jo methods mere andar hain unko ap apne andar bhi bnao



# class Human(ABC): # now this is Abstract class
#     @abstractmethod
#     def walk(self):  # ye method apni child class mein bhi lazim likhna hai warna ye wala use nahi hoga wahn pe
#         pass
    
#     @abstractmethod
#     def eat(self):  # ye strictly follow krwata hai method ke apni child classes mein ye method lazim likhna hai.
#         pass
    
    
# human = Human()
# human.walk()    

#<--------------------------------------------------------------------------->

# class Taha(Human):
#     def __init__(self):
#         self.name = 'Taha'
#         self.age = 20
        
#     def walk(self):
#         print(f"{self.name} is walking")
        
        
        
        
# shobi = Taha()
# print(shobi.name) # Taha
# print(shobi.age)  # 20
# shobi.walk()      # Taha is walking  

#<-------------------------------------------------------------------------->


# class Taha(Human):
#     def __init__(self):
#         self.name = 'Taha'
#         self.age = 20
        
#     def walk(self):
#         print(f"{self.name} is walking")    
        


# taha = Taha()
# taha.walk()


#<-------------------------------------------------------------------------->
# Class Variables

# class Person():
#     last_name = "Ahmed"  # Class Variable
    
    
#     def __init__(self):
#         self.name = "shoaib" # Class attributes
#         self.age = 23
        
        
#     def walk(self):
#         print(f"{self.name} is walking")    
        
        
#     @staticmethod
#     def run():
#         print(f"Person is running")    



# # print(Person.last_name)  # direct print => Ahmed
# # per = Person()
# # print(per.last_name)      # instance print => Ahmed
        
# # per = Person()
# # print(per.run())      # Person is running
                
# Person.run()           # Person is running       



#<-------------------------------------------------------------------------->
# Inspecting Methods with dir()


# class Person():
#     last_name = "Ahmed"  # Class Variable
    
    
#     def __init__(self):
#         self.name = "shoaib" # Class attributes
#         self.age = 23
        
        
#     def walk(self):
#         print(f"{self.name} is walking")    
        
        
#     @staticmethod
#     def run():
#         print(f"Person is running")    



# # print(dir(Person)) # show all methods and class variables but not attributes of cunstructor

# per = Person()
# print(dir(per)) # show all methods and class variables and attributes of cunstructor




#<-------------------------------------------------------------------------->
#  Importing and Using Classes Across Files


# class Person():
#     last_name = "Ahmed"  # Class Variable
    
    
#     def __init__(self):
#         self.name = "shoaib" # Class attributes
#         self.age = 23
        

#<-------------------------------------------------------------------------->
#  Importing and Using Classes Across Files


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        return self.count

    def __str__(self):
        return f"Counter value: {self.count}"

counter = Counter()      # Create an instance of the Counter class

print(counter())       # Uses __call__
print(counter)         # Uses __str__