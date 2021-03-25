#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for k in range(i+1,length):
                if nums[i] + nums[k] == target:
                    return [i,k]

nums = [2, 7, 11, 15]
target = 9

answer = twoSum(nums, target)

print(answer)
