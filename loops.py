# loop  any function that needes to be executed many times.
# while 
#for 
 # while increment will be not be there  untile the condition is met while loop will run all the statements
 
number = [1, 2, 3, 4, 5]
range_value = len(number)
print(range_value)
i = 0
# removing empty string in a list idhi vadutham
while i < -1:
    print(number[i])
    # i += 1

condition_string = ["","sasi","surya","","teja"]
print(condition_string)

while "" in condition_string:
    condition_string.remove("")
print(",".join(condition_string))

# for loop has both intialization and incrementing

#continue 
# break condition

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
condition_string = ["surya","teja","","sasi",""]
for i in range(len(condition_string)):
    if condition_string[i] == "":
        break
    print(condition_string[i])
    
#two Sum 

    # nums = [2, 7, 11, 15]
    # target = 9
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target: 
    #             print(f"The two numbers are {nums[i]} and {nums[j]}")
    #             break                                                                              