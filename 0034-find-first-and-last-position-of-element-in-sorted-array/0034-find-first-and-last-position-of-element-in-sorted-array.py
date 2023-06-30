class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs(nums,target,firstindex):
            l,r=0,len(nums)-1
            i=-1
            while(l<=r):
                m=(l+r)//2
                if nums[m]>target:
                    r=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    i=m
                    if firstindex:
                        r=m-1 #to find the last
                    else:
                        l=m+1 #to find the first
            return i
        
        
        left=bs(nums,target,True)
        right=bs(nums,target,False)
        return [left,right]
                    
                    