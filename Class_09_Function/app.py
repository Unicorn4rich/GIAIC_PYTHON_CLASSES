# example 1

# def namaz():
#     print("wozu")
#     print("niyat")
#     print("namaz")
 
# namaz()    


# example 2
# #                      optional parameter
# def hello(name: str = "No-name"):           # signature
#     print(f"Hello {name}")    # body
    
# hello()       # invoke


# # Example 3: *all_para, => get alla paramaters values.  **extraa => get key value pairs data
# def hello(name: str, age: int, *all_para, **extraa):           # signature
#     print(f"Hello {name}, your age is: {age}")    # body
#     print(all_para)
#     print(extraa)
    
# hello("shoaib", 20, 100, 1010, 99, v1="A", v2="B")       # invoke

# output:
# Hello shoaib, your age is: 20
# (100, 1010, 99)       
# {'v1': 'A', 'v2': 'B'}    


# Example 4

def hello(name: str, age: int):           # signature
    print(f"Hello {name}, your age is: {age}")    # body
   
# positional argument    
# hello(20, "shoaib")          # Hello 20, your age is: shoaib 
hello(age=20, name="shoaib")   # Hello shoaib, your age is: 20
#<------------------------------------------------------------------------------->