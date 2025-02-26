from datetime import datetime, timedelta, date
print(date.today().strftime("%m-%d-%Y"))


# %a
# %A
# %w
# %d
# %b
# %B
# %m
# %y
# %Y
# %H
# %I
# %p
# %M
# %S
# %f
# %z
# %Z
# %j
# %U
# %W
# %c
# %x
# %X
# %%
# %G
# %u
# %V


import math
print(math.pi)
number_list = [1, 2,10, 8,9, 0,11, 12]
print(min(number_list))
print(max(number_list))

number = abs(6.80)
print(math.ceil(number))
print(math.floor(number))
print(math.sqrt(25))
print(math.pow(2,3))


import  json
x = '{"name": "surya", "age": 25, "city":"hyderabad"}'
# y = json.dumps(x)
# print(y)
json_obj = json.loads(x)
print(json_obj)
print(json_obj['name'])
json_obj= json.dumps(json_obj)
print(json_obj[2])

# print(y['name'])
# print(json_obj['name'])




# create module datetimes in side that create a file date_time.py and timedelta.py and date.py
# --> create class DateTimes create a method  retur datetime.now()  
#     create class timedelta create a method  __init__ with hours, minutes, seconds
#     create class Date create a method return date.today()
# %a
# %A
# %w
# %d
# %b
# %B
# %m
# %y
# %Y
# %H
# %I
# %p
# %M
# %S
# %f
# %z
# %Z
# %j
# %U
# %W
# %c
# %x
# %X
# %%
# %G
# %u
# %V

# --> create a module math and file name as math.py andn create a class Math and create method to return square root of a number value self
# --> create a module called json file name json.py and class name as JasonTest and return a json output using json.dumps or json.loads