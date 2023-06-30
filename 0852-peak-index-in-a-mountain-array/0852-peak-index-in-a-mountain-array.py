class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        start=0
        end=len(arr)-1
        while(start<end):
            mid=start+(end-start)//2
            if(arr[mid]>arr[mid+1]):
                end=mid #this can also be the possible sol so end=mid
            else:
                start=mid+1
        return start