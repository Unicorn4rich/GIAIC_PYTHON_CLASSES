class Person():
  "constructor function"

  "attributes"

  "methods"


class Person():
  def __init__(self, my_name: str, ):
    self.name = my_name

  def greeting(self):
    print(f"Hello {self.name}")


p1 = Person("shoaib")
print(p1.name)
p1.greeting()


#--------------------------------------------------------
# inheritance

class Rabia():
  def __init__(self):
    self.cash = "10000"


class Taha(Rabia):
  def __init__(self):
    super().__init__()
    self.name = "shoaib"  

  def balance(self):
    return (f"{self.name} has {self.cash}")    


t = Taha()
print(t.balance())  # shoaib has 10000 



#--------------------------------------------------------
# inheritance 2 paramater

class Rabia():
  def __init__(self, cash: int):
    self.cash = cash


class Taha(Rabia):
  def __init__(self, cash: int, name): # sab se pehly parent ko value denge 
    super().__init__(cash)
    self.name = name  

  def balance(self):
    return (f"{self.name} has {self.cash}")    


t = Taha(30000, "azlaan")
print(t.balance())  # shoaib has 10000 