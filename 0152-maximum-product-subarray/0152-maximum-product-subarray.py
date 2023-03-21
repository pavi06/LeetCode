class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct=max(nums)
        currMax,currMin=1,1
        for i in nums:
            if i==0:
                currMax,currMin=1,1
                continue
            temp=i*currMax
            currMax=max(i*currMax,i*currMin,i)
            currMin=min(temp,i*currMin,i)
            maxproduct=max(maxproduct,currMax)
        return maxproduct
        
        