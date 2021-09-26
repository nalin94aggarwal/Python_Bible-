student = {
    "male":["Tom","Bob","Nick","Frank"],
    "female":["Sarah","Huda","Emma","Gini"]
    }


print(student.keys())


for keys in student.keys():
 for name in student[keys]:
     if "i" in name.lower():
         print(name)
    
    
