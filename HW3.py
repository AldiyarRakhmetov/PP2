import math as m
import random as r
from seperate import seperate

# Python Classes
#1
class StringButNot:
    def __init__(self, str):
        self.value = str
    def getString(self):
        print(self.value)
    def printString(self):
        print(self.value.upper())
    
cl_task1 = StringButNot("test")
cl_task1.getString()
cl_task1.printString()
seperate()

#2
class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
    
cl_task2_1 = Shape()
print(cl_task2_1.area())
cl_task2_2 = Square(14)
print(cl_task2_2.area())
seperate()

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

cl_task3 = Rectangle(11, 32)
print(cl_task3.area())
seperate()

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"This point's coordinates are ({self.x}, {self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        dist = m.sqrt((self.x - other.x) ** 2 - (self.y - other.y) ** 2)
        print(f"distance between these two is: {dist}")
    
cl_task4_1 = Point(1, 1)
cl_task4_1.show()
cl_task4_1.move(2, 3)
cl_task4_1.show()
cl_task4_2 = Point(7, 7)
cl_task4_1.dist(cl_task4_2)
seperate()

#5
class Acount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.money = balance
    def deposit(self, amount):
        self.money += amount
    def withdraw(self, amount):
        if amount > self.money:
            print("unable to withdraw")
        else:
            self.money -= amount

cl_task5 = Acount("Isn't it Account?", 200)
cl_task5.deposit(200)
print(cl_task5.money)
cl_task5.withdraw(350)
print(cl_task5.money)
cl_task5.withdraw(100)
seperate()

#6
def isprime(n):
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, n // 2):
        if n % i == 0:
            return False
    return True

cl_task6 = [i for i in range(1, 101)]
cl_task6_last = list(filter(lambda x : isprime(x), cl_task6))
print(cl_task6_last)
seperate()
seperate()
seperate()

# Python Functions
#1
def americanizer(g):
    print(f"it will be {g * 28.3495231} in american units. 'MERICA!")

americanizer(20)
seperate()

#2
def unamericanizer(F):
    print(f"this will be {(5/9) * (F - 32)} in unamrican units.")

unamericanizer(20)
seperate()

#3
def solve(numheads, numlegs):
    rabbits = (numlegs / 2) - numheads
    chicks = numheads - rabbits
    print(f"there are {int(rabbits)} rabbits and {int(chicks)} chickens")

solve(35, 94)
seperate()

#4
def filter_prime(list):
    newlist = []
    for i in list:
        if isprime(i):
            newlist.append(i)
    return newlist

print(filter_prime([i for i in range(1, 101)]))
seperate()

#5
def permutations_len3(n):
    if len(n) == 1:
        return [n]
    if len(n) == 2:
        N = n[1] + n[0]
        return [n, N]
    if len(n) == 3:
        list = []
        list.append(n)
        a, b, c = n[0], n[1], n[2]
        list.append(a + c + b)
        list.append(b + a + c)
        list.append(b + c + a)
        list.append(c + a + b)
        list.append(c + b + a)
        return list
    
print(permutations_len3("ABD"))
seperate()

#6
def reverstring(str):
    words = str.split()
    rewords = reversed(words)
    for i in rewords:
        print(i, end=' ')
    print()

reverstring("We are so very ready")
seperate()

#7
def has_33(list):
    last_is_3 = False
    for i in list:
        if i == 3:
            if last_is_3:
                return True
            else:
                last_is_3 = True
        else:
            last_is_3 = False
    return False

print(has_33([1, 5, 3, 3, 2]))
print(has_33([2, 3, 5, 3, 1, 1, 3]))
seperate()

#8
def spy_game(list):
    wait = 2
    for i in range(2, len(list)):
        if (list[i - 2], list[i - 1], list[i]) == (0, 0, 7):
            return True
    return False

print(spy_game([1, 0, 0, 7, 8]))
print(spy_game([0, 1, 0, 2, 7, 0, 0]))
seperate()

#9
def sphere_volume(r):
    pi = 3.14
    print(f"around {(4/3) * pi * (r ** 3)}")

sphere_volume(2)
seperate()

#10
def not_a_set_set(list):
    TBR = []
    for i in list:
        if i not in TBR:
            TBR.append(i)
    return TBR

print(not_a_set_set([1, 2, 3, 1, 2, 4, 5, 4, 2]))
seperate()

#11
def ispolyndrome(str):
    streverse = ''
    for i in reversed(str):
        streverse += i
    if str == streverse:
        return True
    else:
        return False
    
print(ispolyndrome("aibohphobia"))
print(ispolyndrome("lmao"))
seperate()

#12
def histogram(list):
    for i in list:
        for j in range(0, i):
            print('*', end='')
        print()

histogram([4, 9, 7, 2, 4])
seperate()

#13
answer = r.randrange(1, 21)
guess_counter = 0
name = input("Hello! What is our name?\n")
print()
print(f"Well {name}, I am thinking of a number between 1 and 20.")
while True:
    guess = int(input(print("Take a guess.\n")))
    if guess == answer:
        print(f"Good job, {name}! You guessed my number in {guess_counter} guesses!")
        break
    else:
        if guess > answer:
            print("Your guess is too high.")
        else:
            print("Your gusee is too low.")
        guess_counter += 1

seperate()

#14 is the seperate function

# Python Functions 2: The Return of Dictionaries
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def isabove5and5(name):
    for i in movies:
        if i["name"] == name:
            if i["imdb"] > 5.5:
                return True
            else:
                return False

print(isabove5and5("We Two"))
print(isabove5and5("Exam"))
seperate()

#2
def allabove5and5():
    for i in movies:
        if i["imdb"] > 5.5:
            print("|", end='')
            print(i["name"], end='|')
    print()

allabove5and5()
seperate()

#3
def allincategory(category):
    for i in movies:
        if i["category"] == category:
            print("|", end='')
            print(i["name"], end='|')
    print()

allincategory("Thriller")
seperate()

#4
def average_imdb(list):
    sum = 0
    count = 0
    for i in list:
        count += 1
        sum += i["imdb"]
    return sum / count

print(average_imdb(movies))
seperate()

#5
def average_of_category(list, category):
    sum = 0
    count = 0
    for i in list:
        if i["category"] == category:
            count += 1
            sum += i["imdb"]
    return sum / count

print(average_of_category(movies, "Thriller"))
seperate()