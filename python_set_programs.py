#set  unordered collection of unique elements
import string

string_set = {"surya", "teja", "yenugula"}
print(string_set)

# accessing
for name in string_set:
    print(name)
    
#add an element or item 
string_set.add("pradeep")
print(string_set)
number_set = {1,2,3,4,3}
#string_set.update(number_set)
string_set.update(number_set)
print(string_set)
combo_list = ["Swetha", "sasi", "prathima", 5,6,7,8,5,6,7]
# set(print()
string_set.update(combo_list)
print(list(string_set)) 

#remove dulicate elements from list without changing the order
               #0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
number_list = [5,1,7,8,3,4,5,8,9,1,4,3,5,6,3]
number_list.sort()
sorted_list = number_list
print(list(set(sorted_list)))
#remove duplicate elements of sorted list
#0 1 2 3 4 5 6 7 8 9 9 10 11 12 13 14
#[1, 3, 4, 5, 6, 7, 8, 9]
from typing import List 
def remove_duplicates(sorted_list:List[int]) -> List[int]:
    index = 1
    for i in range(1,len(sorted_list)):
       if sorted_list[i] != sorted_list[i-1]:
           sorted_list[index] = sorted_list[i]
           index += 1
    return sorted_list[:index]

print(remove_duplicates(sorted_list))

# remove element from set' will throw exception if element is not present
string_set = {"surya", "teja", "yenugula", "pradeep", "prathima", 5,6,7,8}
string_set.remove("surya")
print(string_set)
try:
    string_set.remove("surya")
except KeyError:
    print("element is not present")

 #discard element from set will not throw error if element is not present
string_set.discard("teja")
print(string_set)
string_set.discard("surya")
 #pop element from set random element form set
string_set.pop()
 #clear set
#empty set
string_set.clear()
print(string_set)
 #del it completely removes the set
del string_set
try:
    print(string_set)
except NameError:
    print("set is not defined")
    
    

def get_smalletst_number(nums: List[int]) -> int:
    #time complexity O(N) Space complexity O(1)
    smallest_number = nums[0] #time complexity O(1) Space complexity O(1)
    for num in nums: #time complexity O(N) Space complexity O(1)
        if num < smallest_number: #time complexity O(1) Space complexity O(1)
            smallest_number = num #time complexity O(1) Space complexity O(1)
    return smallest_number
print(get_smalletst_number([5,1,7,8,3,4,5,8,9,1,4,3,5,6,3,-1]))           