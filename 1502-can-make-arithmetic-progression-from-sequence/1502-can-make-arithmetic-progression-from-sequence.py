class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a=sorted(arr)
        d=a[1]-a[0]
        for i in range(1,len(a)-1):
            if a[i+1]-a[i]==d:
                pass
            else:
                return False
        return True
        