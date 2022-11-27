class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dict_1={}
        dict_2={}
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i] in dict_1:
                    return False
                dict_1[s1[i]]=s2[i]
                dict_2[s2[i]]=s1[i]
        if dict_1==dict_2 and len(dict_1)<=2:
            return True
        else:
            return False
            
        