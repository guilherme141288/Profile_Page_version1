class Solution:
    def romanToInt(self, s: str) -> int:
    
        
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        
        ans=0

        
        for i in range(len(s)-1):
            if rti[s[i]] < rti[s[i+1]]:
                ans = ans - rti[s[i]]
            else:   
                ans = ans + rti[s[i]]

        
        return ans+rti[s[-1]]


instance = Solution()
print(instance.romanToInt("L"))