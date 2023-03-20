from typing import List

strs = ["flank","flower","flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    print ("There is no common prefix among the input strings.")
                    return ""
        return prefix
    
instance = Solution()
print (instance.longestCommonPrefix(strs))