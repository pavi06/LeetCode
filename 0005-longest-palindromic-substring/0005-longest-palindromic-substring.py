class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0
        for i in range(len(s)):
            left=right=i
            while( left>=0 and right<=len(s)-1 and s[left]==s[right]):
                if(right-left+1 > reslen):
                    res=s[left:right+1]
                    reslen=right-left+1
                left-=1
                right+=1
            left=i
            right=i+1
            while( left>=0 and right<=len(s)-1 and s[left]==s[right]):
                if(right-left+1 > reslen):
                    res=s[left:right+1]
                    reslen=right-left+1
                left-=1
                right+=1
        return res
        