import json
'''{
    "name" : "shreya" ,
    "isTeacher" : True ,
    "address" : {
        "city" : "mumbai",
        "country" : "India"
         },
    "subjects" : ["python" , "AI/ML"]    
}'''

import json

json_str = '{"name": "shradhha", "isTeacher": true}'

print(type(json_str))

py_obj = json.loads(json_str)

print(type(py_obj))
print(py_obj)
