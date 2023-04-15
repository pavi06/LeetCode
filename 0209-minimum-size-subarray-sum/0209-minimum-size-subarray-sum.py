class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        minsize=float('inf')  #assigning the max value to the minsize var
        total=nums[0]
        while(r<len(nums) and l<=r):
            if total>=target:  #if total is higher than target then incrementing the left pointer by 1
                minsize=min(minsize,r-l+1)   #updating the minsize var
                total-=nums[l]
                l+=1
            else:
                r+=1     #if total is lesser than target then incrementing the right pointer by 1
                if r<len(nums):
                    total+=nums[r]
            
        return minsize if minsize!=float('inf') else 0
        