class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        ma=max(nums)-k
        mi=min(nums)+k
        if mi>ma:
            return 0
        else:
            return ma-mi