"""
"""

str1 = "Python Programming"
str2 = "azaz anowar real"

# Type of str1 and str2
print(str1," is of type ", type(str1))
print(str2," is of type ", type(str2))

#targeting an element by index number [index number stat from 0]
print(str1[5])
# -5 => meaning start from end. when - index start from -1
print(str1[-5])

#slice start index : end index 0-4th element
print(str1[0:5])

# find the index
print(str2.find("w"))

#if the element is not found then -1
print(str2.find("c"))


#print("kaindo na babu \n kaindo na")
# \n for new line
#print("kaindo na babu \"kaindo na\"")
# to print a coute \"

#some useful functons
gan = "Mon Amar Kemon Kemon Kore Re"
print(gan + " bodhu tumi thaiko na baper bari te")
print(gan.lower())
print(gan.upper())
print(len(gan))
print(gan.index("Re"))
print(gan.replace("Re","Pagla"))
