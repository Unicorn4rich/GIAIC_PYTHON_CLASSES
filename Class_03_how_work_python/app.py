name = "Shoaib" # ye naam ram mein jaa kar save hua kisi ram ke box ke child box mein.
print(id(name)) # => 2353860940672 => ye ram ki wo location hai jahn par hmara name ka variable save hua hai.

# name2 = "Azlaan"
print(id(name2)) # 2005238391376 => har variable ki location alag hogi. or jese hi prgram chal ke khatam hoga wo delete ho jaegi ram memory apne ap 

#exponent
num1 = 2
num2 = 3
#                     # 2 = 4 = 8
print(num1 ** num2) # 2 x 2 x 2 = 8


# floor division
num1 = 10
num2 = 3
                   
print(num1 // num2) # => 3 kiyun ke isme floor devision bhi sath ho rhi hai.


# modulus => isko ham seconds or hour ko change karne keliye.
num1 = 300
num2 = 60
                   
# print(num1 % num2) # => 1


# modulus from chat
# Calculate hours, minutes, and seconds from total seconds
total_seconds = 3661  # Example total seconds
hours = total_seconds // 3600 # => 1 Hour
minutes = (total_seconds % 3600) // 60  # 61 // 60 = 1
seconds = total_seconds % 60  # 3661 % 60 = 

print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

# Output: 3661 seconds is equal to 1 hours, 1 minutes, and 1 seconds.


#<-------------------------------------------------------------------------------------->
# Logical

is_true: bool = True
is_false: bool = False

print(! is_true)  #<= ghalat
print(not is_true) #(!)use nahi karty balke true ko false or false ko true karne ke liye (not) lgaty hain.

print(is_true && is_false) #<= ghalat
print(is_true and is_false) # (&&) ko use nahikarte balke uski jagah (and) ko use karte hain.

print(is_true || is_false) # <= ghalat
print(is_true or is_false) # ye tariqa sahi hai 


#<-------------------------------------------------------------------------------------->
# Membership opraters => in & not in

# 1.in => iska matlab hai dhondna matlab ye hamen dhond kar laa kar deta hai.
name = "Shoaib"

# Shoaib ke name ke andar agr (g) ka alphabet aa rha hai to True return karo..
print("g" in name) # => Flase


# 2. not in => iska matlab hai ke ye value check karo
Company = "UniCorn"

print("C" not in Company) # check ki gai value agr moujood hai to ye false return karega.






""" Notes

Cache => Temporary memory save => bar bar api call hogi to hmare prgram ka time delay hoga ham chahty hain Aik dafa Api Call ho 
uske bad api ka sara data Chache ban kar hmari ram ke andar save ho jaye or jese hi ham us api ko call karen to ftafat wo ram mein api 
ka rakha hua data hamen mil jaye.
 ISR component mein jo api data ham kuch der ke liye rokty hain wo data Chache hota hai jo ram ke andar rakha hua hota hai jese hi
hmara set kiyya hua time refresh hota hai to us chache ko ram se delete kar ke dosra chache laya jata hai data se bhara hua isi tarhn
phir har aik chache ke sath hota hai sab. 


How to wrok Python

1. Code Editor => (Cursor Ai) isme ham file (app.py) bana kar kaam karte hain phir
2. Compiler Code ko => (Byte Code) mein compile karta hai for example (0101) phir
3. Vertual Machine => ye hmare binary code ko yani (Byte code) ko samjh kar usy chlati hai.
4. Running Program => vertual machine us binary code ko brwoser par chala deti hai.
5. Vertual Envoirment => Library Modules => isme hmare tamam packages hoty hain hmareproject ke

Point => Cursor Ai mein ham ne aik file bnai (app.py) wo compile ho jati hai (Byte Code) mein yani (0101) phir wo binary code 
vertual mein jata hai wahn se usy binary code mein brwoser par chlaya jata hai.   

"""