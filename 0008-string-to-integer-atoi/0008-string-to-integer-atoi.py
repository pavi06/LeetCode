class Solution:
    def myAtoi(self, s: str) -> int:
        n = s.strip()
        if len(n) == 0:
            return 0
        tmp = "0"
        result = 0
        i = 0
        if n[0] in "+-":
            tmp = n[0]
            i = 1
        for i in range(i, len(n)):
            if n[i].isdigit():
                tmp += n[i]
            else:
                break
        if len(tmp) > 1:
            result = int(tmp)
        if result >(2**31)-1 :
            return (2**31)-1
        elif result < -2**31:
            return -2**31
        else:
            return result
        