# string needs to be in either single quotes or double quotes or Three quotes and Quad quotes

string_var = "Swetha"
multiline_string = """ this python class only gives basic explanation of syntax 
but mainly focuses on actual patterns to implements 
practice all basic core syntax so that you can able to code easily"""
print(string_var[::-1])
print(multiline_string)

# string slicing 
print(string_var[3:])
print(string_var[:4])

print(len(multiline_string))
print(multiline_string[100:120])
# split the string
temp_string_list = multiline_string.split(" ")
print(temp_string_list)
# list is collections of element 
#modify string
# upper() to capitalize string
upper_string = string_var.upper()
print(upper_string)
#lower()
lower_string = upper_string.lower()
print(lower_string)
# removing whitespace
#strip()
white_space_string = " Swetha good night! "
stripped_string = white_space_string.strip()
print(len(white_space_string)>len(stripped_string))
print(white_space_string.strip()) 

# split string 

split_string = "Hello, World! This is a Python String"
split_list = split_string.split(" ")
print(split_list)

# replace
for i in range(len(split_list)):
     split_list[i] = split_list[i].replace("!", "")
     split_list[i] = split_list[i].replace(",", "")
print(split_list)
# concatenate strings
tepm_var = "hello"
temp_name_var = "swetha welcome to the class"

concatenated_string = tepm_var+ " " + temp_name_var
print(concatenated_string)

# format String 
salary = 8000

formatted_string = "Employee Name: {} \nSalary: {}".format("Swetha", salary)
print(formatted_string)
string = f"Employee Name: Swetha \nSalary: {salary}"

print(string)
#excape charcter string
#\
slash_string = "it\'s a \"python\" class"
print(slash_string)
#\\
backslash_string = "it\\s a \"python\" class"
print(backslash_string)

# \n 
newline_string = "hello \n Swetha  \n Surya \n Prathima \n welcome to the class"
print(newline_string)
#\r 

carriage_return_string = "hello \r Swetha"
print(carriage_return_string)
#\t 
tab_string = "welcome to the python \t class"
print(tab_string)
# \b 

backspace_string = "hello \b \bSwetha"
print(backspace_string)

# # binary string 01 2 string 
# 0100

decimal_string = "0-9" # decimal point
#octal value = 0-7 value
hexadecimal_string = "0123456789abcdef"
#\ooo
hexadecimal_string = "\x48"
print(hexadecimal_string)

#string methods
capitalize_string = "capitalize"

print(capitalize_string.capitalize())
# casefolding

print(capitalize_string.casefold())
 # center() 
 # count()
 
 # encode = 
encode_string = "my name is sasi"
encoded_string = encode_string.encode('ascii')
print(encoded_string.decode('ascii'))

#index()

index_string = "hello world"
print(index_string.index('o'))

#isalnum()

isalnum_string = "1234"
print(isalnum_string.isalnum())

# isalpha()
# isdigit()
# isnumeric(print()

#isprintable()
print_able_string = " hello class "+ "123"+""

print(print_able_string.isprintable())

# stip() remove white spaces from a string 
# lstrip() remove left side white spaces of string 

strip_string = " hello world! "
print(strip_string.lstrip())
print(len(strip_string)>len(strip_string.lstrip()))
#rstrip
print(strip_string.rstrip())
#split()

#zfill()

# zfill_string = "123"
# print(zfill_string.zfill(len(zfill_string)+1))


def return_upper_case(string: str):
    return string.upper()
def retun_boolean(string: str):
    return string.isalpha()

