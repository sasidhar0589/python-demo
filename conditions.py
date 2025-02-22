# if first condition else another option od results if  elif  eni condition elif 
number = 20 
number2 = 30 
if number == number2:
    print("both are equal")

elif number > number2:
    print("first number is greater")

elif number < number2:
    print("second number is greater")
else:
    print("both are different")
    
if number != number2: print("first number is not equal to second number")

# ternary operator

result = "First number is greater" if number > number2 else "Both numbers are not equal"
print(result)
condition_string = "jeff went to newyork"
if condition_string is not None and "surya" in condition_string:
    print("Condition string is not empty")
elif(condition_string is not None and "surya" not in condition_string) and ("jeff" not in condition_string):
    print("Condition string does not contains surya")
else:
    print("Condition string is empty")