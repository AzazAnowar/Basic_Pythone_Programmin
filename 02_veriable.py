character_name = "Anowar"
character_age = 500
character_likes ="coding, travel"
is_mail = True
# in python True and False is case sensetiv.

#print("There once was a man nemed " +character_name)
#print("He was "+ str(character_age) + " years old.")
#print("He likes to " +character_likes)
#print("But didn't like being 200.")

#number
num = 7
num1 = -7
print(num," is of type ", type(num))
print(num1," is of type ", type(num1))

# flot
num2 = 10.5
num3 = 10.5
print(num2," is of type ", type(num2))
print(num3," is of type ", type(num3))

#complex number
num4 = 8 + 6j
print(num4," is of type ", type(num4))
# real and imaginary part
print("Real Part is : ",num4.real)
print("Imaginary Part is : ",num4.imag)

# convertion of data types
num5 = 7.8
b = int(num5)
print("After typecasting float: ", num5 ," to int :", b, type(b))

num6 = -90.7
c = int(num6)
print("After typecasting float: ", num6 ," to int :", c, type(c))

num7 = 100
d = float(num7)
print("After typecasting float: ", num7 ," to int :", d, type(d))

num7 = -100
d = float(num7)
print("After typecasting float: ", num7 ," to int :", d, type(d))

# BOOLEAN
is_working = True
is_reading = False
print(is_working," is of type ", type(is_working))
print(is_reading," is of type ", type(is_reading))

# convertion of data types BOOLEAN [False => 0]; [True => 1]
a = int(is_working)
e = int(is_reading)
print(a,e)