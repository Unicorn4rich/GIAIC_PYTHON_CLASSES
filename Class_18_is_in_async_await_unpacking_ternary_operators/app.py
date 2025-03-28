name = "shoaib"
print(id(name))  # memory location => 2085882523568


name1 = "Shoaib"
name2 = "Ahmed"

print(id(name1)) # 2398666911344
print(id(name2)) # 2398668430832


name1 = "Shoaib"
name2 = "Shoaib"

# same values memory mein aik hi store hoti hai or uska refrence alag alag variable print statment ko milta rehta hai.
print(id(name1)) # 2457376943728
print(id(name2)) # 2457376943728


name1 = "Shoaib"

name2 = name1

print(id(name1))  # 2063304191600
print(id(name2))  # 2063304191600


n1 = "Shoaib"
n2 = "Shoaib"

print(id(n1))
print(id(n2))

print(n1 is n2) # 2no ki memory location same hai ya nahi => True


#<--------------------------------------------------------------------------------->
# immutable => str => int => bool
# mutable => list => set => tuple => dict 


# immutable => str => int => bool
# str
n1 = "Shoaib"
n2 = "Shoaib"

print(id(n1))  # 2818524868208
print(id(n2))  # 2818524868208

print(n1 is n2)


# int
n1 = 10
n2 = 10

print(id(n1))     # 140725101032520
print(id(n2))     # 140725101032520
print(n1 is n2)   # True




# mutable => list => set => tuple => dict 


#list
number1 = [1, 2, 3, 4]
number2 = number1

print(id(number1))        # 2281146315264
print(id(number2))        # 2281146315264
  
print(number1 is number2) # True 


number1 = [1, 2, 3, 4]
number2 = [1, 2, 3, 4]

# ye alag alag jagah par save hongi
print(id(number1))        # 1974783799808
print(id(number2))        # 1974783399802
  
print(number1 is number2) # False


# # dict
Person1 = {"name": "shoaib"}
Person2 = {"name": "shoaib"}

print(id(Person1))  # 2903714786816
print(id(Person2))  # 2963716785813

print(Person1 is Person2)  # False


#<--------------------------------------------------------------------------------->
#is = is not


ans = True
print(not ans) # not matlab jo actual value hai uski opposite value dikhaye.


Person1 = {"name": "shoaib"}
Person2 = {"name": "shoaib"}

print(id(Person1))  
print(id(Person2)) 

print(Person1 is not Person2)  # True => ye dono same nahi hain.


#<--------------------------------------------------------------------------------->
# membership operaotor

name = "ABC"

print("E" in name)      # False
print("E" not in name)  # True
print("B" in name)      # True


#<--------------------------------------------------------------------------------->
# async awiat


import asyncio

async def greet():
    await asyncio.sleep(3) # exicutoion mein time delay.
    print("API call no.1")
    
# asyncio.run(greet())  # for single function

# example 2
async def greet_shoaib():
    await asyncio.sleep(7) # exicutoion mein time delay.
    print("API call no.2")



async def main():
    await asyncio.gather(greet(), greet_shoaib())

asyncio.run(main())    



#<--------------------------------------------------------------------------------->
# Unpacking => list

names = ["shoaib", "azlaan", "awais"]

print(names[0])  # shoaib
print(names[1])  # azlaan
print(names[2])  # awais

# unpacking
n1, n2, n3 = names

print(n1) # shoaib
print(n2) # azlaan
print(n3) # awais



#<--------------------------------------------------------------------------------->
# Unpacking => tuple


names = ("shoaib", "azlaan", "awais")

print(names[0])  # shoaib
print(names[1])  # azlaan
print(names[2])  # awais

# unpacking
n1, n2, n3 = names

print(n1) # shoaib
print(n2) # azlaan
print(n3) # awais


#<--------------------------------------------------------------------------------->
# Unpacking => dict

person = {
    "name": "shoaib",
    "age": 23,
}

person["name"]
person["age"]

# unpacking jus keys
value1, value2 = person

print(value1) # name
print(value2) # age


# unpacking just values
value1, value2 = person.values()

print(value1) # shoaib
print(value2) # 23



# example 2
person = {
    "name1": "shoaib",
    "name2": "Ahmed",
}

name1, name2 = person # get keys
name1, name2 = person.values() # get values

print(name1)
print(name2)



#<--------------------------------------------------------------------------------->
# Ternary Operator

result = "condition true" if 2 < 10 else "condition false"
print(result) # condition true

result = "condition true" if 2 > 10 else "condition false"
print(result) # condition false