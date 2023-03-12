class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            ans=int(str(x)[::-1])
        else:
            s=str(x)
            ans=int(s[0]+s[1:][::-1])
        if ans> -2**31 and ans< 2**31-1:
            return ans
        else:
            return 0