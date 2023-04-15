class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d1,res=set(),set()  #creating 2 sets for seen and result
        for i in range(len(s)-9):
            temp=s[i:i+10]
            if temp in d1:
                res.add(temp)
            else:
                d1.add(temp)
        return list(res)
                
        