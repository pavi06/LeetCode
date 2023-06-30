class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l=len(letters)
        start=0
        end=l-1
        while(start<=end):
            mid=start+(end-start)//2
            if(letters[mid]>target):
                end=mid-1
            else:
                start=mid+1
        return letters[start%l];
        