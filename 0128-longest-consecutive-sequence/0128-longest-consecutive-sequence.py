class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=set(nums)
        maxcount=0
        for i in l:
            if i-1 not in l:
                count=0
                while (i+count) in l:
                    count+=1
                
                maxcount=max(maxcount,count)
        return maxcount
                
        