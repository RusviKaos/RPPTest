#Functions 
# def functionName(params):
#sc0pe of params is function

students = []
#Returns list
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

#prints list
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

#variable number of arguments in function
#def var_Kargs(name,id,**kwargs):# * needed in front of param
#    print(name + " " + id)
#    print(kwargs["description"],kwargs["feedback"])# using keywords pased while calling this function

#keyword arguments in function - receiving dictionary
#def var_args(name,id,*args):# * needed in front of param
#    print(name + " " + id)
#    print(args)# * not needed inside

# add_student(name="Mark",student_id=332)# It can be add_student("Mark",332)
# var_args("sale","332","Arg1",None,1,"arg3",True)#passed two "normal" params and 5 arg params
# var_Kargs(name = "sale",id = "332",description = "My Boss",feedback=None, boss = True)

#Adds to list
def add_student(name, student_id=233):
    student = {"name":name,"student_id":student_id} # created dictionary
    students.append(student)
# You can default params - def add_student(name = "Mark", student_id = 332):
# Then no error if add_student() is called without defaulted params

def save_file(student):
    try:
        #if you want to rewrite existing file use "w"
        # "a" is for new or existing file to append data
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save the file")


def read_file():
    try:
        fl = open("students.txt", "r")# "r" read file
        for student in fl.readlines():# list of all lines in file
            add_student(student)
        fl.close()
    except Exception:
        print("Could not read the file")


#student_list = get_students_titlecase()

read_file()
print_students_titlecase()


student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name,student_id)
save_file(student_name)

#q = "y"
#while q == "y":
#    q = input("Enter student? : y/n :")
#    if q == "n" or q != "y":
#        break
#    else:
#        student_name = input("Enter student name: ")
#        student_id = input("Enter student ID: ")
#        add_student(student_name,student_id)
#        save_file(student_name)

#if students:
    #print_students_titlecase()"""



