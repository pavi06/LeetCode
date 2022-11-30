class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def hist(word):
            val,d=[],{}
            i=1
            for w in word:
                if w not in d:
                    d[w]=i
                    i+=1
                val.append(d[w])
            return val
        
        return hist(s)==hist(t)