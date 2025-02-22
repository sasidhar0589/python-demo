#dictionary hastable to be used to store the key value pair
# dictionary is collection of key value pairs with different data types and changeable values
# dictionary = {key:value}
employee_dict = {"name":"surya","salary": 10000,"city": "herendon","state":"VA"}
employee_list_dict= [{"name":"swetha","salary": 10000,"city": "Austin","state":"TX"},{"name":"surya","salary": 10000,"city": "herendon","state":"VA"}]
employee_dict_list ={"name":["surya","swetha"],"salary": [10000,10000],"city": ["herendon","Austin"],"state":["VA","TX"]}
#dictonary of list  or list of dictonaries
print(type(employee_dict))
print(type(employee_list_dict))
print(type(employee_dict_list))
#access 
print(employee_dict_list["name"])
print(employee_dict_list.keys())
temp_list = employee_dict_list.keys()
print(temp_list)
for key in temp_list:
    print(key)
    print(employee_dict_list[key])
    
for key, value in employee_dict_list.items():
    print(key, value)
temp_values = employee_dict_list.values()
print(temp_values)

employee_dict["state"]="CA"
print(employee_dict)
#update
employee_dict.update({"state":"VA"})

# adding an item
employee_dict["gender"] = "M"
print(employee_dict)
# update 
employee_dict.update({"degree": "MS"})
print(employee_dict)

# remove items
#pop(p
employee_dict.pop("degree")

#popitem(employee_dict)
employee_dict.popitem()

#clear employee_dict

# employee_dict.clear()
# print(employee_dict)

#del employee_dict

# del employee_dict

# print(employee_dict)
# copy()
new_employee_dict = employee_dict.copy()
print(new_employee_dict)
# dict()
new_employee_dict1 = dict(employee_dict)
print(new_employee_dict1)
new_employee_dict2 = dict(name="surya", salary=10000, city="herendon", state="VA",degree="MS")
print(new_employee_dict2)

# loop through dictonary

for index in new_employee_dict2:
    print(new_employee_dict2[index])

for index in new_employee_dict2.values():
    print(index)
for key in new_employee_dict2.keys():
    print(key)
for key, value in new_employee_dict2.items():
    print(key, value)
# nested dictonary

nested_dict = {"name":"surya","salary": 10000,"city": "herendon","state":"VA", "address": {"street":"123 Main St","city":"san fransisco","state":"VA"}}

print(nested_dict)
print(nested_dict["address"]["city"])

# nested list

# clear()
# keys()

# values()    

# items()
# copy(print())

# popitem()

# pop(key)
# del()
# update()
# get()
print(nested_dict.get("state"))
#from keys(print(
temp_dict= {"name","age","salary","city"}
value = "surya"
new_dict = dict.fromkeys(temp_dict,value)
print(new_dict)
