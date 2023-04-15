class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r=0,1
        maxsize=1
        prev=""
        while(r<len(arr)): #iterate till end
            if arr[r-1]>arr[r] and prev!=">":
                maxsize=max(maxsize,r-l+1)
                prev=">"
                r+=1
            elif arr[r-1]<arr[r] and prev!="<":
                maxsize=max(maxsize,r-l+1)
                prev="<"
                r+=1
            else:
                r= r+1 if arr[r-1]==arr[r] else r
                l=r-1
                prev=""
        return maxsize
                
#sliding window concept--
#..> < > < > ...
