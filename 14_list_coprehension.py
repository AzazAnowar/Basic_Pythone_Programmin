lst=[]
print(type(lst))

names=["Krish","Jack","Jacob",1,2,3,4,5]
print(names)

mixed_list=[1,"Hello",3.14,True]
print(mixed_list)

### Accessing List Elements
fruits=["apple","banana","cherry","kiwi","guava"]

print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])

print(fruits[1:])
print(fruits[1:3])

### Modifying The List elements
fruits[1]="watermelon"
print(fruits)

fruits[1:]="watermelon"
print(fruits)

fruits=["apple","banana","cherry","kiwi","guava"]

## List Methods

fruits.append("orange") ## Add an item to the end
print(fruits)

fruits.insert(1,"watermelon")
print(fruits)

fruits.remove("banana") ## Removing the first occurance of an item
print(fruits)

## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)

index=fruits.index("cherry")
print(index)

fruits.insert(2,"banana")
print(fruits.count("banana"))

fruits.sort()  ## SSorts the list in ascending order
print(fruits)

fruits.reverse() ## REverse the list
print(fruits)

fruits.clear() ## Remove all items from the list

print(fruits)

## Slicing List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])

#numbers[::3]
#numbers[::-2]

### Iterating Over List

for number in numbers:
    print(number)

## Iterating with index
for index,number in enumerate(numbers):
    print(index,number)

## List comprehension
lst=[]
for x in range(10):
    lst.append(x**2)

print(lst)

lst1 = [x**2 for x in range(10)]
print(lst1)

### Basic List Compression

sqaure=[num**2 for num in range(10)]
print(sqaure)

### List Comprehension with Condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)

print(lst)

even_numbers=[num for num in range(10) if num%2==0]
print(even_numbers)

## Nested List Comphrension

lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair=[[i,j] for i in lst1 for j in lst2]

print(pair)

## List Comprehension with function calls
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 5, 6, 4, 13]