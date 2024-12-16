"""
#### Sets

Sets are a built-in data type in Python used to store collections of unique items.
They are unordered, meaning that the elements do not follow a specific order, and they do not allow duplicate elements.
Sets are useful for membership tests, eliminating duplicate entries, and performing mathematical set operations like union,
intersection, difference, and symmetric difference.

"""

##create a set
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

my_empty_set=set()
print(type(my_empty_set))

my_set = set([1,2,3,4,5,6])
print(my_set)

my_empty_set=set([1,2,3,6,5,4,5,6])
print(my_empty_set)

## Basics Sets Operation
## Adding and Removing Elements
my_set.add(7)
print(my_set)
my_set.add(7)
print(my_set)

## Remove the elements from a set
my_set.remove(3)
print(my_set)

# my_set.remove(10)

my_set.discard(11)
print(my_set)

## pop method
removed_element=my_set.pop()
print(removed_element)
print(my_set)

## clear all the elements
my_set.clear()
print(my_set)

## Set Membership test
my_set={1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)

## Mathematical Operation
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

### Union
union_set=set1.union(set2)
print(union_set)

## Intersection
intersection_set=set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2)
print(set1)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

## Difference
print(set1.difference(set2))

set2.difference(set1)

## Symmetric Difference
set1.symmetric_difference(set2)

## Sets Methods
set1={1,2,3,4,5}
set2={3,4,5}

## is subset
print(set1.issubset(set2))

print(set1.issuperset(set2))

lst=[1,2,2,3,4,4,5]
set(lst)

### Counting Unique words in text

text="In this tutorial we are discussing about sets"
words=text.split()

## convert list of words to set to get unique words

unique_words=set(words)
print(unique_words)
print(len(unique_words))