class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            left=i
            right=i+1
            while(left>=0 and right<=len(s)-1 and s[left]==s[right]):
                left-=1
                right+=1
                count+=1
            left=right=i
            while(left>=0 and right<=len(s)-1 and s[left]==s[right]):
                left-=1
                right+=1
                count+=1
        return count
        