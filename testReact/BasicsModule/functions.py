#Function definition ends with : No need to tell variables what type they are
def add_numbers(a,b):
    return a + b
#Indentation indicates where function ends
print(add_numbers(2,2))#This will work
#print(add_numbers(2,"something"))  -- This won't, Editor or compiler will NOT tell you that
#It will break during run
#Type Hinting can help you visually
def add(a:int,b:int) -> int:#indicating that a and b are int and -> int is returned type
    return a + b
print(add(2,2))#This will work
#print(add(2,"S")) -- This will  NOT work
#So Unit tests will be essential late on with complex code