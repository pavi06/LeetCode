class Solution: 
    def square(self,n:int)->int:
        s=0
        while n:
            rem=n%10
            s+=(rem**2)
            n//=10
        return s
    
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.square(n)
            if n==1:
                return True
        return False
    
    
        