class Person():
  age = 20 # class variable 

  @classmethod # class method bnany ke liye ye decorater lgaenge.
  def bye(cls): # class ki cheezen access karne ke lye ye likhenge self ki jagah class mein.
    return (f"I say bye to. who has age {cls.age}")

  def __init__(self, name):
    self.name = name # instance variable.

  def greet(self):   # instance method.
    return ("hello Nice to meet you")  
  
  @staticmethod
  def hello(a, b):
    return (a + b)

#------------------

shoaib = Person("shoaib") # dont make instance.

print(Person.age) # 20
print(Person.bye()) # I say bye

shoaib = Person("shoaib")
print(shoaib.age) # 20

shoaib = Person("shoaib")
print(shoaib.age) # 20
print(shoaib.bye()) # I say bye

print(Person.bye())# I say bye to. who has age 20

#------------------

shoaib = Person("shoaib")

print(Person.hello(10, 5)) # 15
print(shoaib.hello(10, 5)) # 15

#-------------------------------------------------------------------------------------

def add_greeting(cls):
  cls.greet = lambda x : "hello from Person class"
  return cls

@add_greeting
class Person():
  def __init__(self, name):
    self.name = name

#----------------
azlaan = Person("azlaan")

print(azlaan.greet()) # hello from Person class

#----------------------------------------------------------------

def add_greeting(cls):
  def greet(self):
    return f"hello {self.name}"

  cls.greet = greet
  return cls  


@add_greeting
class Person():
  def __init__(self, name):
    self.name = name

#----------------
azlaan = Person("azlaan")

print(azlaan.greet())




#----------------------------------------------------------------------------------



class Mother():
  def __init__(self):
    self.mother_name = "ammi"
    self.eye_color = "gray"
 
  def greet(self):
    return ("Hello I am mother")


class Father():
  def __init__(self):
    self.father_name = "abbu"
    self.eye_color = "black"

  def greet(self):
    return ("Hello I am father")




class Child(Mother, Father ):
  def __init__(self):
    super().__init__()
    self.name = "azlaan"

  def greet(self):
    return ("Hello i am child")  



print(Child.mro())
print("\n\n")

a = Child()
print(a.eye_color)
print(a.greet())
