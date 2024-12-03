# saying high to the codder
def say_Hi() :
    name = input("Who are you? Enter your Name:")
    print("Oh "+ name + " ! Welcome Back")

#say_Hi()
"""
def cube(num):
    pow(num, 3)
    print(pow(num, 3))

#cube(3)

"""

def cube(num):
    return pow(num, 3)

returned = cube(4)
print(returned)