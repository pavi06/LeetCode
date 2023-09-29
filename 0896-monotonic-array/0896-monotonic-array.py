class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if sorted(nums)==nums or sorted(nums,reverse=True)==nums:
            return True
        else:
            return False
        