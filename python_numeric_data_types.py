"""
Numeric Data types Integers(int), Floats(float()), Complex(complex()) Numbers'
"""


# intger types
postive_intger_number = 10
negative_intger_number = -5


def add(num1, num2):
    return num1 + num2
# num1 - num2
# num1 * num2
# num1 / num2
#num1%num2 reminder of num1/num2
# num1 ** num2
# num1 // num2  quotient of num1/num2


print(add(postive_intger_number, negative_intger_number))


# float types
postive_float_number = 11.9
negative_float_number = -5.1
pi = 3.14
print(add(postive_float_number, negative_float_number))
# integer and float types methods 
# round() rounds nearest integer if a decimal unit is not provided 
print(round(add(postive_float_number, negative_float_number)))
# abs() returns absolute value of a number
print(abs(negative_float_number))
#pow(base, exponent, modules) returns the power of a number
print(pow(int(postive_float_number), 2,5))

# complex types
complex_number = 2j+2j
print(add(complex_number, postive_float_number))

#[j]= sqrt(-5.1*-5.1 +2*2)
print(abs(negative_float_number-2j))

# Assigment Operators  
# =, +=,-+,*=,/=,%=,**=,//= **=,
# 
# &=,|=,^=,>>=,<<=, ==, 
# !=, >, <, >=, <= and, or, not, is, is not, 
# in, not in
#& | ^ ~
# 
# << >> 

# = (assigning a variable)
a_num = 4
b_num = 2
# += (addition and assignment)
# a_num += b_num
# -= (subtraction and assignment)
# a_num -= b_num
# print(a_num)
# *= (multiplication and assignment)
# a_num *= b_num
# a_num &= b_num
# print(a_num)
# a_num |= b_num
# print(a_num)
# a_num ^= b_num
# print(a_num)
# a_num >>= b_num
# print(a_num)
# a_num <<= b_num
if a_num == b_num:
    print("a_num is equal to b_num")
else:
    print("a_num is not equal to b_num")
if a_num != b_num:
    print("a_num is not equal to b_num")
else:
    print("a_num is equal to b_num")
print(a_num>b_num,"A-num is greater than b_num")
if a_num > b_num:
    print("a_num is greater than b_num")
elif a_num < b_num:
    print("a_num is less than b_num")
elif a_num >= b_num ^ a_num <= b_num: # both conditions true will be true both conditions false will be false any of the condition true will be false
    print("a_num is greater than or equal to b_num")

print(a_num is not b_num)