class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i,(w1,w2) in enumerate(zip(word1,word2)):
            s+=w1
            s+=w2
        if word1:
            s+=word1[i+1:]
        if word2:
            s+=word2[i+1:]
        return s