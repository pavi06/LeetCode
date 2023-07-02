class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while(i<len(nums)):
            crt=nums[i]-1
            if nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[crt]:
                nums[i],nums[crt]=nums[crt],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if(nums[i]!=i+1):
                return i+1
        return nums[-1]+1
            
                
        