def seperate():
    print("-----------------------") #That's to make stuff prettier

# HOME, Intro, Get Started
print("Hellooooooooo world!")
print("\nI'm not paid enough for this")
seperate()

#Syntax
a = int(input("gimmie a number: "))
if a > 10:
    print(f"{a} > 10")
elif a < 10:
    print(f"{a} < 10")
else:
    print(f"{a} = 10")
seperate()

#Comments
"""Hi, I'm a weird comment!"""

#Variables
x = input("gimmie anything: ")
print(f"x is {x}, wow!")
x = input("do it again: ")
print('x is now ', x, ', wow!', sep='')
X = input("one more time!: ")
print(f"gotcha! X is not x, thus x is still {x}")

I_exist_000000 = example_yippee = 10
print("\n", I_exist_000000 + example_yippee, "is 20")

print("\nhey, remember that first number you gave?")
def wow_didnt_expect_functions_this_early():
    a = 1j
    print(a, "is not a, yet")
wow_didnt_expect_functions_this_early()
print(f"a = {a}")
def but_alright():
    global a
    a = 1j
but_alright()
print(f"a = {a}. now it is")
seperate()

#Data types
float_var = 0.1
str_var = ":)"
complex_var = 0.1j
none_var = None
dict_var = [0.1, "0.1", 0.1j]
#and others

#Numbers
print("a is currently a complex, right?")
a = 10
float(a) #I wanted to turn 1j into int, but it's impossible. Whoopsie!
print("a =", a)
print("now it's not, and is, in fact, a float")
import random
a = random.randrange(-100, 100)
print(f"and now a is a random value, specifically {a}")
seperate()

#Casting
z = float(4)
print(z)
print("notice that it's '3.0', not '3'")
seperate()

#Strings
stringy = """I won't be used
after this
but it's cool y'all"""
print(stringy)
print()

proper_string = "ExAmPlE1!"
print(proper_string[1], "= 'x'")
print()

for i in proper_string:
    print(i, end=' AND ')
print("stop")
print()

print(f"proper_string's length is {len(proper_string)}")

if "!" in proper_string:
    print("that sure is an excited example string!")
if "?" not in proper_string:
    print("and it's sure in its actions")
print()

print(proper_string[2:5])
print(proper_string[:5])
print(proper_string[-5:-2]) #I'm losing energy, sorry for no funny remarks
print()

print(f"{proper_string.upper()} is {proper_string}, but all caps!")
print()

print("Math" + " with " + "strings??? that sure happened!")
print()
#I've been using format strings this whole time)))
#the \n I've been using here and there are escape characters!
proper_string = proper_string.capitalize()
print(proper_string)
print("hey, look! proper_string was normalized!")
print("what a great way to finish this task!")