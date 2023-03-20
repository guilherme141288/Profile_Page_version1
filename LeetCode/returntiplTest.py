from typing import List

nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        seen = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = (nums[i], nums[j], nums[k])
                    if triplet not in seen:
                        result.append(list(triplet))
                        seen.add(triplet)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return result
    

instance = Solution()
print (instance.threeSum(nums))