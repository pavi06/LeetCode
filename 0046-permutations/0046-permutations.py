# from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # p=permutations(nums)
        # return p
        res=[]
        
        if len(nums)==1:    #if the arr len is 1 then return that ele alone
            return [nums[:]]
        
        for i in range(len(nums)):
            n=nums.pop(0)         #remove the first ele and find all the perumation of remaining elememts
            perms=self.permute(nums)
            
            for i in perms:   #now , add that ele removed to all permutation
                i.append(n)
            res.extend(perms)    #add in the res list
            nums.append(n)       #add that removed ele back to the nums list
        
        return res