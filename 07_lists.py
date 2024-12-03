friends = ["Abul","Babul","Chabul","Dabul"]
#print(friends)
#print(friends[1])
#print(friends[-1])
#print(friends[-2])
print(friends[1:3])
best_friend = friends[1:3]
print(best_friend)

# List Data Types
split1 = "This,is,Orange"
l1 = split1.split(',')
print(l1)
print(type(split1))
print(type(l1))

list2 = ['BD','BDT','+880']
list3 = ['US','USD','+1']

list2 += list3
print(list2)