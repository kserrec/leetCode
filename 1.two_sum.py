# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

# - APPROACHES - 

# 1. Brutce Force, Nested Loops:

# This solution to the "Two Sum" problem involves using a nested loop to iterate over all pairs of numbers in the input list and check if their sum is equal to the target.

# The time complexity of this solution is O(n^2) because the inner loop iterates over all elements of the list for each iteration of the outer loop. This means that the number of iterations grows quadratically with the size of the input list.

# The space complexity of this solution is O(1) because it does not create any additional data structures and only uses a constant amount of memory.

# While this solution is correct and will work for small input lists, it may not be efficient enough for large input lists because of its quadratic time complexity. There are more efficient solutions to this problem that have a linear time complexity, such as the solution that was previously described.


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         for i in range(length):
#             for k in range(i+1, length):
#                 if nums[i] + nums[k] == target:
#                     return [i, k]

# ****************************************************************
# ================================================================
# ****************************************************************

# 2. Dictionary, Single Loop:

# This solution to the "Two Sum" problem involves using a single loop to iterate over the input list of numbers and a dictionary to store the indices of the numbers that have been seen so far.

# The loop starts by initializing an empty dictionary dict. It then iterates over the input list of numbers, using the enumerate function to keep track of the index and value of each number.

# For each number num, the solution checks if target - num is in the dictionary. If it is, then it means that a pair of numbers with the desired sum has been found, and the function returns the indices of these numbers by using the dictionary to look up the index of the other number.

# If target - num is not in the dictionary, then the solution adds num to the dictionary with its index as the value. This allows the solution to keep track of the indices of all the numbers that have been seen so far.

# Once the loop is finished, the function returns an empty list because no pair of numbers with the desired sum was found.

# This solution has a time complexity of O(n) because it only needs to iterate through the list of numbers once. The space complexity is also O(n) because the size of the dictionary grows with the size of the input list.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}  # keep map-bag with values -> index
        for i, num in enumerate(nums):
            if target - num in dict:
                return [i, dict[target - num]]
            else:
                dict[num] = i


twoSumSolver = Solution()

nums = [2, 11, 7, 15]
target = 9

answer = twoSumSolver.twoSum(nums, target)

print("Answer should be: [2, 0]")
print("Answer: ", answer)

# Note:
# It is generally not possible to improve upon the time complexity of the solution that uses a dictionary to store the indices of the numbers that have been seen so far, as it already has a time complexity of O(n).

# However, there are other approaches that can be taken to solve the "Two Sum" problem that may have slightly different space or time trade-offs.

# One alternative approach is to sort the input list of numbers and then use two pointers, one at the beginning of the list and one at the end, to find the pair of numbers that sum to the target. This solution has a time complexity of O(n * log(n)) due to the sorting, but it has a space complexity of O(1) because it does not use any additional data structures.

# Another approach is to use a hash table to store the numbers and their indices. This solution has the same time complexity as the dictionary-based solution, but it may have a slightly lower space complexity because a hash table typically uses less memory than a dictionary.

# Ultimately, the best solution will depend on the specific requirements and constraints of your problem. You may want to consider factors such as the size of the input, the allowed time and space complexity, and the performance requirements of your application when deciding which approach to use.





