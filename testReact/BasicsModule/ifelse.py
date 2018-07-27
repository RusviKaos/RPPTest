name = "Dave"
machine = "HAL"
sentence = None

#If Else ends with : and indentation defines scope of if and else
if machine == "HAL":
    print("{0} I wil Kill You".format(name))
else:
    print("{0},You are safe".format(name))

if name:#This is True
    print("name defined and true")

#text #variable with no definition will give out an error
text = "1"
if text:#This will be false if text = "" or text = None 
    print("text defined and true")

num = 5 
if num:#This is True for ANY int value except 0 or None
    print("has number of value {0}".format(num))

if num == 5:# !=5 will be false
    print("This is true")

n1 = True
n2 = False

if n1:
    print("This is True")

if not n1:
    print("This is false")

if num == 5 and n1:# and instead of &&
    print("This is True")

if num == 0 or n1: #or insteat of ||
    print("This is True also")

print(int(n1))# = 1
print(int(n2))# = 0

print(str(n1))# = True
print(str(n2))# = False
#So be carefull using "if" on numbers without giving it condition
#otherwise you are checking boolean
q = 1
w = 2
#onliner of if else (True result infront if, False result after else)
print("bigger" if q > w else "smaller")# = smaller