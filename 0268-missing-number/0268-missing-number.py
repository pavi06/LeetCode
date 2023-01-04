class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i in nums:
                continue
            return i
        return len(nums)
    
    #((n * (n+1)) // 2) - sum(l) 
        