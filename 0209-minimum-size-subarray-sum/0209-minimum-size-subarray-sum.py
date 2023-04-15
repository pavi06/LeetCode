class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        minsize=float('inf')
        total=nums[0]
        while(r<len(nums) and l<=r):
            if total>=target:
                minsize=min(minsize,r-l+1)
                total-=nums[l]
                l+=1
            else:
                r+=1
                if r<len(nums):
                    total+=nums[r]
            
        return minsize if minsize!=float('inf') else 0
        