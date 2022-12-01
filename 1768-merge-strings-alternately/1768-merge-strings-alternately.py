class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i in range(len(word1) if len(word1)<len(word2) else len(word2)):
            s+=word1[i]
            s+=word2[i]
        if word1:
            s+=word1[i+1:]
        if word2:
            s+=word2[i+1:]
        return s