class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        ma=max(nums)-k
        mi=min(nums)+k
        if mi>ma:  #whenever this is true we can make ele same val thus resultant will be 0
            return 0
        else:     #simply return the diff
            return ma-mi