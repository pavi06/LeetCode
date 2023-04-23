class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])
#O(nlogn), O(1)
        