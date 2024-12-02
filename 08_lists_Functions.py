friends = ["Abul","Babul","Chabul","Dabul","Dabul","Abul"]
lucky_numbers = [4,8,15,16,23,42]

print(friends)
print(lucky_numbers)

#friends.extend(lucky_numbers)
#print(friends)

friends.append("kana")
print(friends)

friends.insert(2,"Modna")
print(friends)

friend_removed1 = friends.remove('Dabul')
print(friend_removed1)

#friends.clear()

removed_friend = friends.pop()
print(removed_friend)
print(friends)

#find if the element is in the list
print(friends.index("Babul"))

print(friends.count("Abul"))

friends.sort()

lucky_numbers.reverse()

print(friends)
print(lucky_numbers)

lucky_numbers2= lucky_numbers.copy()
print(lucky_numbers2)