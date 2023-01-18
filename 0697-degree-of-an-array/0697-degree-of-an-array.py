class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count,start,end={},{},{}
        for i in range(len(nums)):
            if nums[i] not in count:   #if not exist creating with 1 
                count[nums[i]]=1        #assign start and end index to i 
                start[nums[i]]=i
                end[nums[i]]=i
            else:
                count[nums[i]]+=1     #if exist adding the count by 1
                end[nums[i]]=i          #alter the end index alone
        res=[]
        m=max(count.values())   #storing maximum count value 
        for i,j in count.items():
            if j==m:
                res.append((end[i]-start[i])+1)    #adding all length of sub arrays
        return min(res)  #returning min len of subarray
            