import json
student = {
    "Age":20,
    "Good_student":False,
    "Name":"qlkwje",
    "Grades":[1,2,1,2,2,1],
    "Appear":{
                "Hair":"Blonde",
                "Height":"183cm",
                "Eyes_color":"Blue"
            }
}
file = open("student.json", "w") 
  
json.dump(student, file, indent = 6) 
  
file.close()