def add(a:int,b:int) -> int:
    return a + b
print(add(2,2))

name = "Sale"
machine = "HAL"

print("Hello {0}\nMy name is {1}".format(name,machine))

if machine == "HAL":
    print("HAL Will Kill You")
else:
    print("You are safe")

if name:
    print("name defined and true")

text =""

if text:
    print("text defined and true")

num = 0
if num:
    print("has number of value {0}".format(num))