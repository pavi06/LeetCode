class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        s=0
        for i in range(1,len(nums)+1):
            s=0
            for j in range(0,i):
                s+=nums[j]
            l.append(s)
        return l