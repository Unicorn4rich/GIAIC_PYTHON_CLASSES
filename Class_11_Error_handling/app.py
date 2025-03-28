state = "Working"
print("😈 Hello Taha")

try:
    print("😍", state / 0)    
except:
    print("Apke code mein error hai") 
        
print("🤢 Bye Taha")

# Output: 
# 😈 Hello Taha
# Apke code mein error hai
# 🤢 Bye Taha    

#<------------------------------------------------------------------------------------->

print(10 / 0)

nums_list = [1, 23, 4, 55] # 0 => 3

print(nums_list[7])                         # IndexError: list index out of range


my_dict = {"name": "shoaib", "age": 12}
print(my_dict["fullName"])                  # KeyError


my_name = "shoaib"

my_Number = int(my_name)                     # ValueError

#<------------------------------------------------------------------------------------->

try:
    nums_list = [1, 23, 7, 90]
    print(nums_list[6])
    
except Exception as e:  
    print("apke code mein error hai: ", e)  
    print("save to db", e)
    
print("Hello shoaib")    



try:
    print(10 / 0)            # agr code sahi chala to
    
except Exception as e:  
    print("I am Exeption")  
else:    
    print("I am else")       # else bhi chlaega kiyun ke isme ham koi dosra kaam bhi krwa rhy hoty hain jese file open close karna.
finally:
    print("This code always exicute")

#<------------------------------------------------------------------------------------->

