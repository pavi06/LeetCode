class Solution:
    def signFunc(self,n):
        if n>0:
            return 1
        elif n==0:
            return 0
        else:
            return -1
        
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        for i in nums:
            prod*=i
        return self.signFunc(prod)
    
    
        