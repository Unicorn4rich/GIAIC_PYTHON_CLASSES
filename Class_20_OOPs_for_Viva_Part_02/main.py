# property ke method se ham access kar paenge priavte attribute ko or method ke naam ke sath setter likh denge @balance.setter to usy ham modify kar sakty hain or del se delete kar sakty hain.

class Person():
  def __init__(self, name, amount=0):
    self.name = name
    self.__balance = amount

  @property  # is method ko () laga kar nahi balke simple balance likh kar bhi access kar sakty hain decorater ki wajah se.
  def balance(self):
    return self.__balance

  @balance.setter    # opar waly function ke naam se usme value set kar rhy hain.
  def balance(self, value):
    if value > 0:
      self.__balance += value
      print(f"Your new balance is {self.__balance}")


  @balance.deleter 
  def balance(self):
    del self.__balance   

#----------------------------------------
shoaib = Person("shoaib", 4000)

shoaib.balance = 100

print(shoaib.balance) # value dekhny ki koshish karenge to opar wala method chalega or agr value set karenge to neechy wala method chal jaega automaticly.

del shoaib.balance # is line ko likhenge to opar wala delte ka method chalega.


try:
  print(shoaib.balance)
except Exception as e:
  print("This property is not available")  



# ----------------------------------------------------------------
# collable
# metaclass => create class => object/instance


class Person():
  def __init__(self, name):
    self.name = name

  def __call__(self): # ye method instance ko callble bnata hai aisy => shoaib()
    return "This class is for Person name" 

  def __str__(self): # ye instance ko without
    return ("I am str method")  


#-------------------------
shoaib = Person("shoaib") # instance/object
# print(shoaib()) # direct instance callable => This class is for Person name

print(shoaib) # direct instance ko without () callable => This class is for Person name


#----------------------------------------------------------------
# Error handling

class WrongDivison(Exception):
  pass

class Divide():
  def __init__(self):
    pass

  def calculate(self, val1, val2):
    if val2 == 0:
      raise WrongDivison("Cannot devide by Zero")
    else:
      result = val1 / val2
      print(result)

#-------------------------------------------------------

my_cal = Divide()

try:
  my_cal.calculate(10, 0)
except WrongDivison as e:
  print("Error", e)
  
  
#----------------------------------------------------------------
# Abstract Class => make not instance
from abc import ABC, abstractmethod


class Animal(ABC):
  @abstractmethod
  def speak():
    pass


class Dog(Animal):
  def __init__(self):
    self.name = "dazy"

  def speak(self):
    pass   


dog = Dog()


#----------------------------------------------------------------
# 


class Person():
  def __new__(cls): # ye empty object create karta hai or init se pehly ye chalta hai.
    print("I am new")

  def __init__(self, name): # instance bnata hai.
    print("after new, my job is to add attribute in the form of property in that empty object")

    self.name = name


shoaib = Person("azlaan")



# example 2

class Person():
  def __new__(cls, value): # ye empty object create karta hai or init se pehly ye chalta hai.
    print("I am new")
    return super().__new__(cls)

  def __init__(self, name): # instance bnata hai.
    print(" I am init")
    self.name = name

  def __del__(self):
    print("I am del")  


shoaib = Person("azlaan") # ye argument init se pehly new mein jata hai uske bad init ke pass jata hai

del shoaib
del shoaib  


#-----------------------------------------------------------------------------------------------

# Composeesion 
# Strong Realtionship => parent class kokuch hua to child class error dey degi

class Person():
  def __init__(self):
    self.name = "shoaib"

  def info(self):
    print("I am shoaib")  


class Company():
  def __init__(self):
    self.employe = Person() # ye as a object ban kar pass hui => {name: "shoaib"}


c = Company()
c.employe.info()  # I am shoaib 

#----------------------------------------------------------------------------------
# Aggregation
# Week Realtionship   => parent class kokuch bhi hua to child class phir bhi chalegi.


class Student():
  def __init__(self, name):
    self.name = name

class School():
  def __init__(self, students=None):
    self.students = students


s1 = Student("azlaan")  # {"name":"azlaan"}  
s2 = Student("ajju")    # {"name":"ajju"}     


sch = School([s1, s2]) # agr ye argument nahi bhi denge to object phir bhi create hoga

print(sch.students)