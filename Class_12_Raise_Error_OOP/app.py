# Raising a Custom Error:


# try:
#     raise("I am rasing a Error") # ye keyword error genrate arta hai
# except Exception as e:
#     print("try has error: ", e)


#example 2

# class shoaibError(Exception):
#     pass

# try:
#     raise shoaibError("This is a TahaEror error message.") # ye keyword error genrate arta hai
# except shoaibError as e:
#     print(f"Cought TahaError: {e}")  # Cought TahaError: This is a TahaEror error message.
    
    
    
#<--------------------------------------------------------------------------------->    
# OOP

# 1. data/attributes
# 2. methods 
# 3. manipulate that data
# 4. instances 
# 5. classes



# Class
class Human(): # class have (2) things => (1.data => variable/attributes) = (2.methods => functions)
    
    # Constructor function
    def __init__(self, bahr_wala_name: str):    # constructor function => beech ka matlab class se cheezen ley kar object ko deta hai or object se cheezen ley kar class ko. 
        self.name = bahr_wala_name         # name => is a variable/data/attribute


# Instance of class
# Object
human1 = Human("azlaan") # instance => matlab class se bana hua object.
print(human1.name) # azlaan

human2 = Human("shoaib")
print(human2.name) # shoaib