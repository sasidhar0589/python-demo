#write a program to reverse the list
numbers = [1, 2, 3, 4, 5]
#excepted output [5,4,3,2,1]

# def reversing_list(numbers):
#     numbers.sort(reverse=True)
#     return numbers
# # def reverse_list(numbers):
# #     return numbers[::-1]
#                     #    -1
# numbers = [1, 2, 3, 4, 5]
# # numbers[:-1]
# print(numbers[::-1])

# print(reverse_list(numbers))

# def reverse_list(numbers):
#     numbers.reverse()
#     return numbers

# reversed_list = reverse_list(numbers)
# print(reversed_list)

def reverse_list(numbers):
    reversed_list = []
    # range(0, len(numbers,1)
    for i in range(len(numbers)-1, -1, -1):
        reversed_list.append(numbers[i])
    return reversed_list
print(reverse_list(numbers))
    
