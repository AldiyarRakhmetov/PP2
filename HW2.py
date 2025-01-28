def seperate():
    print("-----------------------") #That's to make stuff prettier, again

# Booleans
Aldiyar = "molodets"
print(bool(Aldiyar)) # I am true
print(Aldiyar == "bad student") # And I'm not a bad student
seperate()

# Operators
print(3 % 2) # Remainder, answer is 1
print(3 // 2) # Floor division, answer is 0
print(3 ** 2) # Exponent, answer is 9
print(9 >= 8 and 9 >= 9) #True!
print(3 + (3 + 2) - 3 * 2) # Ordering is important
seperate

# Lists
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False] #lists can be of any type

list4 = ["aboba", 228, 1337j] #and have any values

print(type(list4)) #lists are their own thing
# type of arrays are tuple, dictionary, sets and lists
print(list2[2]) # Gives 3rd element
print(list1[-1]) # Gives the last element, -2 will give second to last
longlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(longlist[2:5]) # You can select a part of a list
print(f"{longlist[:5]} and {longlist[2:]}")
if 1337j in list4:
    print("You can also see whether the element is in a list or not")
print()

list1[1] = "cavendish"
print(f'{list1} <- WOW! You can change values in a list!!!!')
longlist[2:5] = ["even", "its", 'chunks', "with", "any number of things"]
print(longlist)
list3.insert(2, True) #you can also add an element wherever
list3.append(True) # though this is the easiest way
list4.extend(list3) #you can also combine the lists, and even other arrs
print(list4)
print()

list4.remove(True) #you may also remove stuff
list4.pop(1) #pop() will pop the last element
# you could also do "del list4[1]"
# "del list4" will empty it out, "list4.clear()" will too
print(list4)
print()

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #looptyloop
for i in range(len(thislist)):
  print(thislist[i]) #looptyloop via index
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 # while looptyloop 
[print(x) for x in thislist] #list comp
print()

newlist = [x if x != "banana" else "orange" for x in thislist]
print(newlist)
#whoa! conditionals!
print()

list2.sort()
print(list2) #lists may be sorted
print(sorted(longlist))
list4.reverse()
print(list4) #they can also be reversed
print()

list4copy = list4.copy()
#you can also copy a list with list4[:] or list(list4)
seperate()

# Tuples
thistuple = ("apple",)
print(type(thistuple)) #this is a tuple
thistuple = ("apple")
print(type(thistuple)) #this is *not* a tuple
similiartolists = (23, "lol", None, True)
print()

#Tuples can't be changed once made, though when it comes to accessing
#They are the same as lists

#A workaround the unchanging nature of tuple is to
actuallylist = list(similiartolists) #turn tuple into a list
actuallylist[3] = False #change the temp list
similiartolists = tuple(actuallylist) #and change it back to tuple
print(similiartolists)
print()

(num, string, void, bul) = similiartolists #unpacking
print(num, string, void, bul)
(thing, *otherthings) = similiartolists
print(thing, otherthings)
(leftmost, *mid, rightmost) = similiartolists
print(leftmost, mid, rightmost)
print()
#Tuples loop like lists

thistuple = ("apple",)
frankestein = thistuple + similiartolists #joining tuples
print(frankestein)
seperate()

# Sets
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print()

thisset.add("to add something, you use add, not append")
what_list = ["and to combine them", "you use update"]
thisset.update(what_list)
print(thisset)
print()

thisset.remove(1) #same can be done with discard(1)
#BUT if there won't be 1 in thisset, discrad wil not
#raise an error, whilst remove will
thisset.pop() #this one's random
#Looping is the same as lists
print(thisset)
print()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"a", "d", "f"}
set4 = {2, 4, 6}

unionset = set1.union(set2, set3, set4)
print(unionset) # | also means "union"
intersectionset = set1.intersection(set3)
print(intersectionset) # & also means "intersection"
differenceset = set1.difference(set3)
print(differenceset) # - also means "difference"
symdifset = set1.symmetric_difference(set3)
print(symdifset) # ^ also means "symmetric difference"
print()

# Dictionaries
thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["colors"]) #alternitevly "thisdict.get("colors")"
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
print()

thisdict["colors"] = "none lol" #alt: thisdict.update({"colors": "none lol"})
thisdict["driver"] = "Bongibanga" #update can be used there
thisdict.pop("electric") #del can also be used
#thisdict.popitem() will remove the driver
#Loops same as lists via keys
for x, y in thisdict.items():
  print(x, y) #But you can also do this!
#Can also be copied similiar to lists

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} #Nests!
seperate()

# If...Else
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
a /= 10
if not a > b:
  print("a is NOT greater than b")
#pass can be used to make if statement do nothing
seperate()

# While Loops
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# continue will make loop skip to next iterator
# break will make the loop stop
seperate()

# For Loops
for x in range(2, 30, 3):
  print(x)
else:
  print("For Loops can be nested, as in there's a for loop in a for loop")
seperate()