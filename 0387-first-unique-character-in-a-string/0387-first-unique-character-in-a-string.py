class Solution:
    def firstUniqChar(self, s: str) -> int:
        flag=0
        for i,j in enumerate(s):
            if s.count(j)==1:
                return i
        return -1
        