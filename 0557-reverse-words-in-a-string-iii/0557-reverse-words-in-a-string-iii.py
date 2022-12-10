class Solution:
    def reverseWords(self, s: str) -> str:
        s1=""
        for i,j in enumerate(s.split(" ")):
            s1+=j[::-1]
            s1+=" "
        return s1.strip()
        