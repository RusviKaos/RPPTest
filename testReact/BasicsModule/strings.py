#Strings
#You can use single ,double or tripple quotes
#There are no multiline comments but if you write :
"""This is a comment and it is  a string also
that python will recognize if we assign a variable to it.
otherwise python treats this as a comment"""

#Some usefull functions of wich there are many

print("hello".capitalize())#All to CAPS = HELLO
print("hello".replace("e","a"))#replace letters or strings = hallo
print("hello".isalpha())#Check if all chars in string are letters = True
print("hello1".isalpha())#Check if all chars in string are letters = False
print("123".isdigit())#Check if all chars in string are numbers = True
print("123a".isdigit())#Check if all chars in string are numbers = False
print("name1,name2,name3".split(","))#Split string in array of strings = ["name1","name2","name3"]

name = "Dave"
machine = "HAL"
sentence = None
#format function can receive indefinite number of params
#here inside string by defining {0} {1} {2} ... is coresponding
#to order of variables in format function
sentence = "Hello {0}\nMy name is {1}".format(name,machine)
#print(sentence)
#or print directly without new variable (sentence)
print("Hello {0} My name is {1}".format(name,machine))

#different way if for f to stand in front of string and inside {} variable name is used
sentence = f"Hello {name}\nMy name is {machine}"
#print(sentence)
#or print directly without new variable (sentence)
print(f"Hello {name} My name is {machine}")