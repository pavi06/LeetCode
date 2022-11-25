class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)[2:]
        l=len(s)
        s1='0'*(32-l)+s
        return s1.count('1')
        