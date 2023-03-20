
from typing import List

nums = [2,7,11,15]
target = 18

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through every pair of numbers in the list
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # check if the sum of the current pair is equal to the target
                if nums[i] + nums[j] == target:
                    # if it is, return the indices of the two numbers
                    return [i, j]
        
        # if no two numbers add up to the target, return an empty list
        return []

instance = Solution()
print(instance.twoSum(nums , target))    