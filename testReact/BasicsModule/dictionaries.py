#Dictionaries (keys and values)
# simple dictionary 
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
#Get values
print(student["name"])# = Mark
#print(student["last_name"]) KeyError if there is no key
#avoid by get("key","default value") 
print(student.get("last_name","Unknown_key"))# = Unknown_key
#get keys
print(student.keys())# returns list of keys
#get values
print(student.values())# returns list of values
#Change value
student["name"] = "James"
print(student)
#deleting keys
del student["name"]
print(student)
#List of dictionaries
all_students = [
    {"name": "Mark", "student_id": 15163,"feedback": None},
    {"name": "Katarina", "student_id": 63112,"feedback": None},
    {"name": "Jessica", "student_id": 30021,"feedback": None}
]
for s in all_students:#itterate through dictionary list
    print(s)# print(s["name"])


