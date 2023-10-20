class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        opened=0
        closed=0
        start=0
        for i in range(len(s)):
            if s[i]=='(':
                opened+=1
            elif s[i]==')':
                closed+=1
            if opened==closed:
                res+=s[start+1:i]
                start=i+1
                opened=0
                closed=0
        return res
                
        