class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s=sorted(nums)[::-1]
        for i in range(len(s)-2):
            if s[i ]< (s[i+1]+s[i+2]):
                return s[i]+s[i+1]+s[i+2]
        return 0
            
        
        
            
        