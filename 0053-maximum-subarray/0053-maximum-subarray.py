class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]  #assigning to the initial value
        currsum=0
        for i in nums:
            if currsum<0:  #if negative then the var is resetted to 0
                currsum=0
            currsum+=i
            maxsum=max(maxsum,currsum)
        return maxsum
    
#sliding window