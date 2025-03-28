# class Person():
#     father = "shoaib"
    
    
#     def __init__(self):
#         self.name = "John"
#         self.age = 36
        
#     def greet(self):
#         print(f"Hello {self.name}")
        
#     @staticmethod    
#     def hello_static():
#         print("Hello from static method")    
        
        
        
        
# # print(Person.father)  # shoaib
# # Person.greet()        # error
# Person.hello_static()   # Hello from static method



#<-------------------------------------------------------------------------->
# Dunder function


# class Person():
    
#     def __init__(self):
#         self.name = "shoaib"
#         self.age = 23
        
#     def __call__(self):        # dunder function
#         print("This is a Person class and it has shoaib and 23 ")
        
        
# per = Person()
# # print(per())  # error => without call method
# # per()         # after define call method => This is a Person class and it has shoaib and 23 
# # per.__call__()  # This is a Person class and it has shoaib and 23 
        
        
        
#<-------------------------------------------------------------------------->


# class Person():
    
#     def __init__(self):
#         self.name = "shoaib"
#         self.age = 23
        
        
# per = Person()
# print(dir(per))      
# # Output
# """
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']

# """


#<-------------------------------------------------------------------------->


# class Person():
    
#     def __init__(self):
#         self.name = "shoaib"
#         self.age = 23
        
#     def __str__(self):
#         return f"Hello I am Person method"    
        
        
        
# per = Person()
# print(per)         # Hello I am Person method  
# print(Person())    # Hello I am Person method 



#<-------------------------------------------------------------------------->
# File Handling

# # file.txt mein data write kar rhy hain is file mein rehty huy.
# # with open("file ka naam", "uske sath karna kya hai")
# with open("file.txt", "w") as f:
#     f.write(""" Hello world 
#  I am Shoaib
#  My age is 99 """)



# # 2sri file ka data yahn laakar Read karne walay function se data dekh rhy hain.
# with open("file.txt", "r") as f: # file ko lao mujhe usy parhna hai.
#     result = f.read()
#     print(result)   # I am Shoaib => ye line fil.txt ke andar likhi hui thi.
    
    
    
    
#<-------------------------------------------------------------------------->
# Decorators function


# # jab mai nahi chahta hmara function modify ho jata hai to usko decorator ke andar likhna hota hai.
# def decorator(func): # <= ye greet() function hai as a parameter.
#     def wrapper():
#         print("I am opper wala decorator")  # greet() function se pehly ye code chalega
#         func()  # greet() function ka sara code yahn chalega
#         print("I am neechy wala decorator") # greet() function ke bad ye code chalega
    
#     return wrapper


# @decorator  # isko decoratore function ko as paramater pass kar diyya
# def greet():    # main function jiske opar oe neechy kuch or bnana hai.
#     print("Hello Python")
    
    
# greet()  


# # output

# # I am opper wala decorator
# # Hello Python
# # I am neechy wala decor



#<-------------------------------------------------------------------------->
# generator function


# aik function ke andar se multiple return karwa sakty hain.
def greet():
    yield "Hello"
    yield "Bye"
    yield "My name"
    yield "is shoaib"
    yield "tum kon ho"
    
    
grt = greet()
print(next(grt))  
print(next(grt))  
print(next(grt))  
print(next(grt))  
print(next(grt))  
# print(next(grt))  # extra print error


# output:
    
# Hello
# Bye       
# My name   
# is shoaib 
# tum kon ho    