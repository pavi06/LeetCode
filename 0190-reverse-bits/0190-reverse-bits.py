class Solution:
    def reverseBits(self, n: int) -> int:
        num=bin(n)[2:]
        rev=num[::-1]+'0'*(32-len(num))
        return int(rev,2)
        
        