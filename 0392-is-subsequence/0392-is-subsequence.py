class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0   #making use of two pointer and iterate over the strings
        while i<len(s) and j<len(t):
            if s[i]==t[j]:   #if both strings are ssame increment i and j ,if not increment j alone
                i+=1
            j+=1
        if i==len(s):
            return True
        else:
            return False
            
        