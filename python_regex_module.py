import re
txt = """ hello swetha welcome to python class
 hello surya welcome to python class
"""
temp_str = re.findall("surya?",txt)
temp_str1 = re.search("\s",txt)
temp_str1 = re.search("swetha",txt)
temp_str2= re.split("\s",txt,2)
print(temp_str2)
print(temp_str1)
print(temp_str)

temp_str3 = re.sub("surya","surya teja",txt)
temp_str3 = re.sub("\w+","sasi" ,txt)
txt = "hello swetha welcome to python class"
temp_str4 = re.search(r"\bp\w+",txt)

print(temp_str4.group())

re.compile(r"\bp\w+")
# print(temp_str3) 