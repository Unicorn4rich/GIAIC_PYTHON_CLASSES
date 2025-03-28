# class Person():
#     def __init__(self):
#         self.name = "shoaib"
#         self.age = 20
        
    
#     # def __call__(self):     
#     #     # Allows the object to be called as a function
#     #     return (self.name, self.age)   
    
#     def __str__(self):
#         # Defines how the object is printed
#         return f"Vector({self.name}, {self.age})"    
    
   
# per1 = Person()
# print(per1)



#<----------------------------------------------------------------------------------------------->
# The Four Pillars of OOP

# 1.Inheritance    => single Inheritance/Multiple Inheritance  => Inheritance allows a class to inherit attributes and methods from another class.
# 2.polymorphism   => Method overriding/duck typing  => Polymorphism allows a class to take on multiple forms.
# 3.Encapsulation  => Encapsulation allows a class to hide its implementation details.
# 4.Abstraction    => Abstraction allows a class to hide its implementation details.

# Polymorphism =>
# Polymorphism allows methods to do different things based on the object calling them. This can be achieved through      method overriding and dynamic behavior (duck typing).


# Animal Classes with Method Overriding

# example 1
class Animal:
    def speak(self):
        return "Animal speaking"
    
    
# example 2    
class Dog(Animal):
    def speak(self):
        return "Woof!"    


# example 3
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
    
# example 4
def animal_sound(animal: Animal):
    # Polymorphic function that works with any Animal subclass
    print(animal.speak())       


dog = Dog()
cat = Cat()

animal_sound(dog) # Woof!
# animal_sound(cat) # Meow!





#<----------------------------------------------------------------------------------------------->
# polymorphism
# poly  => many
# morph => behavier


# example 1
# class Animal:
#     def speak(self):
#         return "Animal speaking"
    
    
# # example 2    
# class Dog(Animal):
#     def speak(self):
#         return "Dog bhaou!"  
    
    
 
# animal = Animal()
# dog = Dog()

# print(animal.speak()) # Animal speaking
# print(dog.speak())    # Dog bhaou!



#<----------------------------------------------------------------------------------------------->
# Duck Typing


# example 1
class Animal:
    def speak(self):
       pass
    
 
    
# example 2    
class Dog():
    def speak(self):
        return "Dog speaking!"  
    

# example 3
class Cat():
    def speak(self):
        return "Cat speaking!"
    
 
def animal_sound(animal: Animal):
    # Polymorphic function that works with any Animal subclass
    print(animal.speak())   
    
 
dog = Dog()
cat = Cat()  
  
animal_sound(dog)  
animal_sound(cat)  