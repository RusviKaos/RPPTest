student_names = ["sale","aco","toni"]
#For loop (end with :) this one is like For Each
#every itteration fills {0} with Sname variable
#no need to tell for loop where to start and where to end
for Sname in student_names:
    print("{0}".format(Sname))

x = 0
for index in range(10):#range - itterate 10 times
    x += 1
    print("x = {0}".format(x))
print("")
x = 0
for index in range(1,6):#range - itterate 5 times (0,5),(5,10)...skip those not in range
    x += 1
    print("x = {0}".format(x))
print("")
x = 0
for index in range(0,10,2):#range - itterate 10 times, execute every 2
    x += 1
    print("x = {0}".format(x))
print("")

#Let's see it with list
lst = [0,1,2,3,4,5,6,7,8,9]

for index in range(10):#either know your list length or use len(lst) function to get it
    print("{0}".format(lst[index]))
print("")

for index in range(1,6):
    print("{0}".format(lst[index]))
print("")

for index in range(0,10,2):
    print("{0}".format(lst[index]))
print("")

for index in range(0,10,3):
    print("{0}".format(lst[index]))
print("")

#Break and Continue in for loops
name_list = ["sale","rade","aco","toni","josip","babic","matori","novi"]

#searching for element in list
for usr_name in name_list:#not optimized, goes through entire list
    if usr_name == "toni":
        print("Found "+ usr_name)
    print("testing " + usr_name)
print("")
for usr_name in name_list:#optimized to break from loop when condition is met
    if usr_name == "toni":
        print("Found "+ usr_name)
        break
    print("testing " + usr_name)
print("")
#searching for everything except element in list
for usr_name in name_list:#optimized not to execute code when condition is met
    if usr_name == "toni":
        continue
        print("Found "+ usr_name)
    print("getting " + usr_name)
print("")

#While loop 
x = 0
while x < 10:
    print("Count is {0}".format(x))
    x +=1










