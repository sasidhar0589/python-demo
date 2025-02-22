
# list tuple set dictonary

# list is collection of items(any data type)
# n number of items
  #             0 1 2 3 4 5 6 7 8 9           
numeric_list = [1,2,3,4,5,6,7,8,9,10]
print(numeric_list[2:4])
print(numeric_list[-4:-2])
numeric_list.append(11)
# insert into numeric_list
numeric_list.insert(0, 12)
print(numeric_list)
#extend numeric_list
string_list = ["surya", "teja", "yenugula"]
numeric_list.extend(string_list)
string_tuple = ("surya", "teja", "yenugula")
numeric_list.extend(string_tuple)
print(numeric_list)
# remove from numeric_list items
numeric_list.remove(12)
print(numeric_list)
# pop from numeric_list index(memory location)
numeric_list.pop(12)
print(numeric_list)
#del numeric_list it will also remove specific index
del numeric_list[10]
print(numeric_list)

# #clear numeric_list
# numeric_list.clear()
# print(numeric_list)


#loopiing
# print(len(numeric_list))
# for num in numeric_list:
#     print(num)
#start of the index to end of the index # incremernt 
# for index in range(1,len(numeric_list),2):
#     print(numeric_list[index])
# index =0
# while index < len(numeric_list):
#     print(numeric_list[index])
#     index += 1
#list comprehension []
number_list = [num for num in numeric_list  if isinstance(num, int)]
surya_list  =  [num for num in numeric_list if isinstance(num, str)]

# num_list = []
# for num in numeric_list:
#     if isinstance(num, int):
#         num_list.append(num)
# print(num_list)
#sorting default ascending

number_list.sort(reverse=True)
print(number_list)
string_list.append("prathima")
string_list.sort(reverse=True)
# print(string_list)
# copy String list
sorted_list  = string_list.copy()
print(sorted_list)

# list () 
string_tupe = "sasi","surya","teja","prathima","swetha"
print(type(string_tupe))
print(type(list(string_tupe)))
#join list 
combined_list = number_list+string_list
string = combined_list.index("teja")
print(string)



# append()
# insert()
# extend()
# remove()
# pop()
# del()
# clear()
# sort()
# copy()
# list()
# index()
#len()
