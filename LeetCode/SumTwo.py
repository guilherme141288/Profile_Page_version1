

from typing import List

nums = [2,7,11,15]
target = 9
complement_dict = {}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:




    # loop through the list of numbers
        for i, num in enumerate(nums):
        # calculate the complement of the current number
            complement = target - num
        
        # check if the complement is already in the dictionary
            if complement in complement_dict:
            # if it is, return the indices of the two numbers
                return [complement_dict[complement], i]
        
        # if the complement is not in the dictionary, add the current number and its index to the dictionary
        complement_dict[num] = i
    
    # if no two numbers add up to the target, return an empty list
        return [] 


instance = Solution()
print(instance.twoSum(nums, target))

