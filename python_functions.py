#  function or method is a block of code it runs only when it is called 
#  we can pass parameters as arguments into a function or method
# function can return or not return
from typing import Dict
def greet(name):
    print("Hello", name)
    return get_name(name)
def get_name(name):
    return "bye, "+name

names = ["surya", "teja", "yenugula","sasi","swetha"]

def get_phone_number(name: str)->Dict:
    temp_dict = {}
    phone_number = {
        "surya": 1234567890,
        "teja": 1234567890,
        "yenugula": 1234567890,
        "sasi": 1234567890,
        "swetha": 1234567890
    }
    temp_dict[name] = phone_number[name]
    return temp_dict

for name in names:
    print(get_phone_number(name))
get_phone_number("name")