# sum of a list
# two sum of a list
from typing import List

# space complexity
#time complexity
# time complexity and space represents big O notation
# two sum proble  
"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 N = number of INTEGERS in the list
 target = sumation of two list items
 expected output = indices of the two numbers that add up to target

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 """
 
 
def two_sume(nums: List[int], target: int) -> List[int]:
    
    
    for index in range(len(nums)): #time complexity O(N) Space complexity
        for incremented_index in range(index+1, len(nums)): #time complexity O(N)*O(N) = O(N^2) 
            if nums[index]== target - nums[incremented_index]: #time complexity O(1) Space complexity O(1)
                return [index, incremented_index]
    return []
print(two_sume([2,7,11,15], 25))
print(two_sume([3,2,4], 6))
print(two_sume([3,3], 6))
print(two_sume([9,11,13,15,17],20))
def two_sum(nums: List[int], target: int) -> List[int]:
    #time complexity O(N) Space complexity O(N)
    nums_dict = {} #time complexity O(1) Space complexity O(1)
    for index, num in enumerate(nums): #time complexity O(N) Space complexity O(N)
        if target - num in nums_dict: #time complexity O(1) Space complexity O(1)
            return [nums_dict[target - num], index]
        nums_dict[num] = index
    return []
print(two_sum([2,7,11,15], 25))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))
print(two_sum([9,11,13,15,17],20))


def sum_of_list(nums: List[int]) -> int:
    #time complexity O(N) Space complexity O(1)
    sum = 0 #time complexity O(1) Space complexity O(1)
    for num in nums: #time complexity O(N) Space complexity O(1)
        sum += num #time complexity O(1) Space complexity O(1)
    return sum

def sumes_of_list(nums: List[int]) -> int:
    #time complexity O(N) Space complexity O(1)
    return sum(nums) #time complexity O(N) Space complexity O(1)