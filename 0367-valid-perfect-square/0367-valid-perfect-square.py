import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if pow(int(math.sqrt(num)),2)==num:
            return True
        return False
        