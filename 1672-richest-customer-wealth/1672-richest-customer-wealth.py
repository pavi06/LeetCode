class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            s=sum(i)
            if s>m:
                m=s
        return m
            
        