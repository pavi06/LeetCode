class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def hist(nums):
            d={}
            for i in nums:
                if str(i) not in d:
                    d[str(i)]=1
                else:
                    d[str(i)]+=1
            return d
        res=hist(nums)
        res=sorted(res.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
        l=[int(i[0]) for i in res] 
        return l[:k]
        
                    
        