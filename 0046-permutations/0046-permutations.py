from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p=permutations(nums)
        return p