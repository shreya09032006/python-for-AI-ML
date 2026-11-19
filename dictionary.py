#dictionary 

info = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(type(info)) 
 # Output: <class 'dict'>

info["age"] = 31
print(info)

#type casting 

dict_keys = list(info.values())
print(dict_keys)  # Output: ['John', 31, 'New York']


#methods
#keys method
print(info.keys())  # Output: dict_keys(['name', 'age', 'city'])
#values method
print(info.values())  # Output: dict_values(['John', 31, 'New York'])
#items method
print(info.items())  # Output: dict_items([('name', 'John'), ('age', 31), ('city', 'New York')])
#get method
print(info.get("name"))  # Output: John
#update method
info.update({"age": 32, "city": "Los Angeles"})
print(info)  # Output: {'name': 'John', 'age': 32, 'city': 'Los Angeles'}