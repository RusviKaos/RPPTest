#Exceptions
student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

#last_name = student["last_name"] - gives KeyError

#Like try/catch
try:
    last_name = student["last_name"]
except KeyError:
    print("No last name")

#(chaining different exceptions)
student["last_name"] = "Batarelo"
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("No last name")
except TypeError as error:#This will give me more detail about error
    print("Cant add str and int " + error)#print out error
except Exception:
    print("Unknown error")