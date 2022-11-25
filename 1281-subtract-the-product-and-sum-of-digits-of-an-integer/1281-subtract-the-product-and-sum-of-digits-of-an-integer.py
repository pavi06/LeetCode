class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1
        while(n>0):
            t=n%10
            s+=t
            p*=t
            n//=10
        return p-s
        