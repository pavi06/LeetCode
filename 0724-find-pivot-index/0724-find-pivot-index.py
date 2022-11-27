class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        total=sum(nums)
        for i in range(len(nums)):
            rsum=total-nums[i]-lsum
            if(lsum==rsum):
                return i
            lsum+=nums[i]
        return -1
                
        