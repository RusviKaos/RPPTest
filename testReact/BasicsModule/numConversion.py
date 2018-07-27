#Integers and floats
answer = 42
pi = 3.14159
#No need for conversion here
print(answer + pi)# = 45.14159
#You can force conversion by putting type in front of bracket sorounded variable
print(int(pi) + float(answer))# 3 + 42.0 = 45.0
print(str(pi) + str(answer))#this just combines strings = 3.1415942
#print(str(pi) + float(answer)) This won't work, can't add str and float