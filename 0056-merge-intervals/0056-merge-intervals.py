class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])  #list is sorted based on the start value
        res=[intervals[0]]   #output list is stored with first ele
        for start,end in intervals[1:]:     #iterate over all ele in the list
            k = res[-1][1]   #last ele end value is stored
            if start<=k:     #k is checked with  next ele start value 
                res[-1][1]=max(end,k)         
            else:
                res.append([start,end])   #if interval can't be merged then the list is appended.
        return res
                
            
        