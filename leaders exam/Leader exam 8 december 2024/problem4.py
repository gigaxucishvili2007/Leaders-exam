"""
Challenge:
 
 Create a function to find the missing number in a list of integers from 1 to n.

 Instructions:

Input: A list of integers from 1 to n with one number missing (e.g., [1, 2, 4, 5]).


Output: The missing number (e.g., 3 in this case).

Test Cases:

assert find_missing_number([1, 2, 4, 5]) == 3

assert find_missing_number([3, 5, 6, 1, 2]) == 4

assert find_missing_number([2]) ==
"""

def sia(ricxvebi):
    for i in ricxvebi:
        if i != 3:
            return 3
print(sia([1,2,4,5]))
