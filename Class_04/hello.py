# .lower()
# Definition: String ke sare uppercase letters ko lowercase mein convert karta hai.

text = "HELLO WORLD"
# print(text.lower())  # "hello world"

#Use Case: User input ko lowercase mein convert karne ke liye, taake comparison easy ho.


#<----------------------------------------------------------------------------------->
# .upper()
# Definition: String ke sare lowercase letters ko uppercase mein convert karta hai.

text = "hello world"
# print(text.upper())  # "HELLO WORLD"

#Use Case: Important text ya headings ko uppercase dikhane ke liye.


#<----------------------------------------------------------------------------------->
# .capitalize()
# Definition: Sirf pehla letter uppercase karta hai, baqi sab lowercase ho jate hain.

text = "hello WORLD"
# print(text.capitalize())  # "Hello world"


#Use Case: Names ya sentences ke first letter ko uppercase karne ke liye.


#<----------------------------------------------------------------------------------->
#  .title()
# Definition: Har word ka pehla letter uppercase karta hai.

text = "hello world"
# print(text.title())  # "Hello World"

#Use Case: Book titles ya blog headings formatting ke liye.


#<----------------------------------------------------------------------------------->
# .strip()
# Definition: String ke start aur end se extra spaces remove karta hai.

text = "  Hello World   "
# print(text.strip())

#Use Case: User input se extra spaces hatane ke liye.

#<----------------------------------------------------------------------------------->
# .index()
# Definition: Kisi character ya substring ka pehla occurrence index return karta hai.

text = "Hello World"
# print(text.index("o")) # 4

#Use Case: Kisi specific character ki position find karne ke liye.

#<----------------------------------------------------------------------------------->
# .count()
# Definition: Ek character ya substring kitni dafa mojood hai, yeh return karta hai.

text = "Hello World"
# print(text.count("o")) # 2

#Use Case: Kisi word ya letter ki frequency check karne ke liye


#<----------------------------------------------------------------------------------->
# .replace() => given 2 values
# Definition: Ek substring ko dusri substring se replace karta hai.

text = "Hello World"
# print(text.replace("World", "Shoaib")) #Hello Shoaib

#Use Case: Strings mein unwanted words replace karne ke liye.


#<----------------------------------------------------------------------------------->
# .split()
# Definition: String ko chhoti chhoti substrings mein tod kar ek list return karta hai.

text = "Hello World"
# print(text.split(" ")) # => ['Hello', 'World']

# Use Case: CSV data ya user input ko process karne ke liye.


#<----------------------------------------------------------------------------------->
# .join()
# Definition: Ek list ke elements ko concatenate karke ek string bana deta hai.

words = ["hello", "World"]
# print(" ".join(words)) # hello World



#Use Case: Lists ko ek single string mein convert karne ke liye.

#<----------------------------------------------------------------------------------->
# .isalnum()
# Definition: Check karta hai ke string sirf alphabets aur numbers pe مشتمل hai ya nahi.


words2 = "Hello123"
# print(words.isalnum()) # True

# Use Case: Usernames ya passwords ki validation ke liye.


#<----------------------------------------------------------------------------------->
# name = input("What is your name?: ")
# print(f"This is userName: {name}")

text = "Hello World"
# print(text.upper())                    # Output: HELLO WORLD
# print(text.replace("World", "Python")) # Output: Hello Python

#<----------------------------------------------------------------------------------->
# Rounding a float

rounding = 2983.4675
# print(round(rounding, 2)) # 2983.47


#<----------------------------------------------------------------------------------->
# list

my_list: list[str] = ["shoaib", "azlaan", "sahil", "khan"]

# print(my_list[2])

#<----------------------------------------------------------------------------------->
# list and methods

fruits = ["apple", "banana", "cherry"]

# fruits.append("orange") # ['apple', 'banana', 'cherry', 'orange'] => list ke last mein value ko add kar dega.
# print(fruits)

# fruits.insert(1, "mango") # ['apple', 'mango', 'banana', 'cherry'] => jo index number denge us index pe add karega.
# print(fruits)


fruits2 = ["apple2", "banana2", "cherry2"] # for extend method
# fruits.extend(fruits2) # ['apple', 'banana', 'cherry', 'apple2', 'banana2', 'cherry2'] => first list ke andar second list ko add kar dega
# print(fruits)

# fruits.pop(1) # ['apple', 'cherry'] => last mein se ya btaye huy index ki value delete karega.
# print(fruits) 

# fruits.remove("banana") # ['apple', 'cherry'] => name se delete kar dega.
# print(fruits)

# fruits.sort()
# print(fruits) # ['apple', 'banana', 'cherry'] => alphabet sequence mein karega.

# numbers = [5,2,3,9,8,0]

# numbers.sort()
# print(numbers) # [0, 2, 3, 5, 8, 9]

# fruits.reverse()
# print(fruits) # ['cherry', 'banana', 'apple'] => z se a ki tarf karega

# numbers = [5,2,3,9,8,0,1]

# print(numbers[2:5]) # [3, 9, 8] => btai hui values nikal kar dega.


#<----------------------------------------------------------------------------------->
# loop
# Definition: Iterates over items of a sequence.

names = ["shoaib", "azlaan", "sahil", "khan"]

# for name in names:
#     pass # loop bad mein use karna hai to uske error ko stop kar sakty hain.


# for index, name in enumerate(names): # ye loop value ke sath uska index number bhi genrate krta hai.
#     print(index, name)
    
# Output:
# 0 shoaib
# 1 azlaan
# 2 sahil 
# 3 khan     


# for name in names: # ye loop value ke sath uska index number bhi genrate krta hai.
#     print(name)
# else:
#     print("loop completed") # loop chalne ke bad har haal mein ye else bhi chalega.
    
# for name in names:
#     print("Hello", name)
#     if name == "azlaan":
#         break
# else:
#     print("Value is not here")    
 
# Output:
# Hello shoaib
# Hello azlaan  


#<----------------------------------------------------------------------------------->
# while loop          
# Definition: Repeats as long as a condition is true.

count = 1

# while count <= 5:
#     print(count)
#     count += 1


#<----------------------------------------------------------------------------------->
# pip install streamlit