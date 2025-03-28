# OOP => Object Oriented Programming
# 1. Class
# 2. data/attributes
# 3. methods 
# 4. manipulate that data
# 5. instances 
# 6. classes
# 7. inheritance => single & multiple



# # Class
# class Human(): # class have (2) things => (1.data => variable/attributes) = (2.methods => functions)
    
#     # Constructor function  => iske (self) ke andar hi Attribute or methods hoty hain jinge ham dot laga kar access karte hain.
#     def __init__(self, bahr_wala_name: str):    # constructor function => beech ka matlab class se cheezen ley kar object ko deta hai or object se cheezen ley kar class ko. 
#         self.name = bahr_wala_name         # name => is a variable/data/attribute
#         self.age = 10
        
#     def walk(self, isAlive: bool):     # walk => is a method/function
#         print(f"{self.name} iswalking... and he is {self.age} year old")
#         print(isAlive)
        
        

# # Instance of class
# # Object
# human1 = Human("azlaan") # instance => matlab class se bana hua object.
# print(human1.name)   # azlaan
# print(human1.age)    # 10
# # print(human1.walk()) # azlaan iswalking... and he is 10 year old => None kiyun ye method print ke andar rakha hai or is method se kuch return nahi ho rha to None aega.
# human1.walk(True)        # azlaan iswalking... and he is 10 year old => None is no more without print.


#<-------------------------------------------------------------------------------------->
# single Inheritance example


# # Class
# class Human(): # class have (2) things => (1.data => variable/attributes) = (2.methods => functions)
    
#     # Constructor function  => iske (self) ke andar hi Attribute or methods hoty hain jinge ham dot laga kar access karte hain.
#     def __init__(self, bahr_wala_name: str):    # constructor function => beech ka matlab class se cheezen ley kar object ko deta hai or object se cheezen ley kar class ko. 
#         self.name = bahr_wala_name         # name => is a variable/data/attribute
#         self.age = 10
        
#     def walk(self):     # walk => is a method/function
#         print(f"{self.name} is walking... and he is {self.age} year old")
       
        
        
# # Example Class 3        

# # inherit Human class
# class Student(Human): # student class Human class ke functions or variables ko apne andar ley kar aa jaega.
    
#     def __init__(self, bahr_wala_name: str, bahar_wali_Id: int): # opar waly constructer ka paramater bhi yahn required hoga.
#         super().__init__(bahr_wala_name)     # super method ka use karte huy hamne opar waly constructor ko ye paramater opar bheja hai.
#         self.student_id = bahar_wali_Id


#     def Student_info(self):
#         print(f"{self.name} is a srudent and his age is {self.age} and Id {self.student_id}")
    
    

# stud1 = Student('Ali', 12345)

# print(stud1.name) # Ali
# print(stud1.age)  # 10
# print(stud1.student_id)  # 12345
# stud1.walk()      # Ali is walking... and he is 10 year old => come frpm Human() class.
# stud1.Student_info() # Ali is a srudent and his age is 10 and Id 12345 => Student() class ka apna method hai ye.



#<-------------------------------------------------------------------------------------->
# multiple Inheritance example

#  Father Class 1
class Father():
    
    def __init__(self, father_Name: str):
        self.father_name = father_Name
        
        
    def show_father_name(self):
        return f"Father`s Name: {self.father_name}"    
    
    def eye_color(self):
        return "blue"
    
    
    
    
# Mother CLass 2
class Mother():
    
    def __init__(self, mother_Name: str):
        self.mother_name = mother_Name     
        
    def show_mother_name(self):
        return f"Mother`s Name: {self.mother_name}"
          
    def eye_color(self):
        return "black"    
        
        


# Child Class 3
class Child(Father, Mother):  # jo class pehly likhi hogi or agr un classes ke andar same values methods waly methods hain to jo class pehly likhi hogi usi ki property milegi.
    
    def __init__(self, father_name: str, mother_name: str, child_Name: str):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)    
        self.child_name = child_Name  
        



# isinstance/object

# child_1 = Child("John", "Alice", "Bob")
# print(child_1.show_father_name()) # Father`s Name: John => from Father() class.
# print(child_1.show_mother_name()) # Mother`s Name: Alice => from Mother() class.
# print(child_1.child_name)         # Bob => from itself


# another example
child_2 = Child("John", "Alice", "Bob")
print(child_2.eye_color())    # blue => from Father() class ka eye_color() method se mila is child ko.