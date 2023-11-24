class Solution:
    def checkPalindrome(self,l,r,s,res):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if(r-l+1 > len(res)):
                res=s[l:r+1]
            r+=1
            l-=1
        return res,len(s)

    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            l,r=i,i
            r1,rl1=self.checkPalindrome(l,r,s,res)
            if(rl1>len(res)):
                res=r1
            l,r=i,i+1
            r1,rl1=self.checkPalindrome(l,r,s,res)
            if(rl1>len(res)):
                res=r1
        return res
        