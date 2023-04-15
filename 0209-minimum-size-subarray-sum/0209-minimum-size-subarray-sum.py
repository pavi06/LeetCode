class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        minsize=float('inf')
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                minsize=min(minsize,r-l+1)
                total-=nums[l]
                l+=1
            
        return minsize if minsize!=float('inf') else 0
        