from seperate import seperate as sep
from seperate import hyperseperate as hysep
import os as o
import os.path as op
import time
import math

# Python File Handling
THEpath = 'C:\\Users\\Aldiy\\work'

#1
task1 = [f for f in o.listdir(THEpath) if op.isfile(op.join(THEpath, f))]
print(*task1)
sep()

#2
print(o.access(THEpath, o.F_OK))
print(o.access(THEpath, o.R_OK))
print(o.access(THEpath, o.W_OK))
print(o.access(THEpath, o.X_OK))
sep()

#3
if o.access(THEpath, o.F_OK):
    print(o.path.basename(THEpath))
    print(o.path.dirname(THEpath))
sep()

#4
THEtext = open("HW6_txt.txt", "r+")
print(len(THEtext.readlines()))
sep()

THEtext.close()

#5
reading = open("HW6_txt.txt", "r")
# reading.write("\nline made for task5")
print(reading.readlines())
hysep()

#6
task6_letter = ord("A")
try:
    task6 = open("HW6_" + chr(task6_letter) + ".txt", "x")
    task6.close()
except:
    pass
else:
    for i in range(0, 25):
        task6_letter += 1
        task6 = open("HW6_" + chr(task6_letter) + ".txt", "x")
        task6.close()

#7
task7_txt = open("HW6_txt.txt", "r+")
task7_A = open("HW6_A.txt", "r+")
for x in task7_txt:
    task7_A.write(x)
task7_txt.close()
task7_A.close()

#8
task8_letter = ord("A")
if o.path.exists("HW6_A.txt"):
    o.remove("HW6_A.txt")
    for i in range(0, 25):
        task8_letter += 1
        o.remove("HW6_" + chr(task8_letter) + ".txt")

# Python Bult-In Functions
#1
task1_list = [3, 5, 6, 9]
task1_c = 1
for i in range(0, len(task1_list)):
    task1_c *= task1_list[i]
print(task1_c)
sep()

#2
task2_string = "LOL, lmao even"
task2_U = 0
task2_l = 0
for i in task2_string:
    if i.isalpha() and i == i.upper():
        task2_U += 1
    if i.isalpha() and i == i.lower():
        task2_l += 1
print(f"There are {task2_U} uppers and {task2_l} lowers")
sep()

#3
task3 = ["banana", "detartrated"]
task3_ans = []
for i in task3:
    if i == i[::-1]:
        task3_ans.append(True)
    else:
        task3_ans.append(False)
print(task3_ans)
sep()

#4
task4_num = 1254
task4_sec = 1254
time.sleep(task4_sec * 0.001)
print(f"Square root of {task4_num} after {task4_sec} miliseconds is {math.sqrt(task4_sec)}")
sep()

#5
task5 = [(1, "Hello", True), (1, "Goodbye", False)]
task5_ans = []
for i in task5:
    task5_ans.append(all(i))
print(task5_ans)
hysep()