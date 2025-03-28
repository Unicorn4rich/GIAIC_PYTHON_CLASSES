


name_list = ["Shoaib", "Ahmed"]

set_comp = {name.lower()   for name in name_list}
# print(set_comp)
print(type(set_comp))


# lambda  "Params"  :  "Code"
my_name_func = lambda  name, age  :  print(name, age)

my_name_func("Taha", 20)


#<----------------------------------------------->
#Map => Itration + new modifiend list
#Map is a class object


name_list = ["sHoaib", "ahmed"]

# map( "function",  "list" )
mew_list = list(map( lambda x : x + " Khan" ,  name_list ))

print(mew_list)


#<----------------------------------------------->
# Filter (Filter Values)

name_list = ["shoaib", "ali", "khan", "taha"]

# filter(   "function",     "list"   )
new_filter_list = list(filter(lambda x : x != "taha", name_list))

print(new_filter_list)


#<----------------------------------------------->
#Reduce (Reduce Iterable to Single Value)

from functools import reduce

number_list = [5, 3, 2]

# reduce(             "function"                   "list")
total_amount = reduce(lambda x, y : x + y ,    number_list)

print(total_amount) # from functools import reduce
