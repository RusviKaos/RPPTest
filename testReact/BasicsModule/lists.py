#LISTS or ARRAYS(Called lists from now on)
student_names = ["sale","aco","toni"]#declare array
print(student_names[0])#print first element = sale
print(student_names[-1])#print last element, very useful = toni
#ADD ELEMENT TO LIST
#student_names[3] = "Homer" is NOT allowed
student_names.append("Homer")#add element to end of list

print(student_names) # = ["sale","aco","toni","Homer"]
print(len(student_names))# len(list) gives number of elements = 4

print("sale" in student_names)# True if sale is in list = True

del student_names[1] #deletes element at position 1 list moves to the left
print(student_names) # = ["sale","toni","Homer"]

#SLICING LIST
print(student_names[1:])# Start list from element at position 1 = ['toni', 'Homer']
print(student_names[1:-1])# Start list from element at position 1 and finish before last one = ['toni']
