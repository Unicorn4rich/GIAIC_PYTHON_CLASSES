# Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}

new_set = set1 | set2
print(new_set)

print(set1 | set2)


#<------------------------------------------------------------------------->
# Intersection

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

my_set = set1 & set2
print(my_set) # {3, 4}


#<------------------------------------------------------------------------->
# Difference 

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

my_set = set1 - set2
print(my_set) # {1, 2}


#<------------------------------------------------------------------------->
# Eliminating Duplicates from a List

name_list = ["taha", "ahmed", "khan", 'taha', 'ahmed']

unique_list = list(set(name_list))
print(unique_list)  # for just set => {'ahmed', 'taha', 'khan'}
print(unique_list)  # again convert in list => ['ahmed', 'taha', 'khan']



#<------------------------------------------------------------------------->
# Dictionary (Key-Value Pairs)

my_dict: dict[str, str|int] = {
    "name": "shoaib",
    "age": 12
}

print(my_dict["name"]) # shoaib
my_dict["isAlive"] = True
print(my_dict)  # {'name': 'shoaib', 'age': 12, 'isAlive': True}

del my_dict["age"]
print(my_dict) # {'name': 'shoaib'}

my_dict.pop("isALive", None)
print(my_dict) # {'name': 'shoaib', 'age': 12}

print(my_dict.pop("isALive", None)) # None

print(my_dict["isAlive"]) # KeyError: 'isAlive'

print(my_dict.get("isALive", "not found")) # not found



#<------------------------------------------------------------------------->
# Iterating Over Keys (Default Behavior)

my_dict: dict[str, str|int] = {
    "name": "Taha", 
    "age": 22, 
    "city": "Lahore"
    }

for key in my_dict: # only keys
    print(key)
    
for key in my_dict: # key values
    print(key, my_dict[key])
    
for key in my_dict.values(): # values
    print(key)
    
for key, value in my_dict.items(): # key values
    print(key, value)
    
    
    
#<------------------------------------------------------------------------->
#  Comprehensions

names_list = ["shoaib", "khan", "Heera", "laal", "ahmed"]

# my_comprehensions = ["code"          "loop"         "extra condition"]  
my_comprehensions = [item.capitalize()    for item in names_list    if item != "khan"]  

print(my_comprehensions)  # opar wali values neechy aa gai => ['Shoaib', 'Heera', 'Laal', 'Ahmed']


#<------------------------------------------------------------------------->
# Dictionary Comprehension

my_dict: dict[str, str|int] = {
    "name": "Taha", 
    "age": 22, 
    "city": "Lahore"
    }

# name_dict = {                   "Code"                       "loop"                     "condition"}
name_dict: dict[str, str|int] = {key:value       for key, value in my_dict.items()     if value == "Taha"} 

print(name_dict)  # only condition value titeld hogi => {'name': 'Taha'}


