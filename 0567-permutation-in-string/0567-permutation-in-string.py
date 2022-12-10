class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        
        # initial values for first set of window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2)-len(s1)):  # n2-n1 is the number of slides
            if s1Count == s2Count:
                return True
            
            # reduce leaving char count
            s2Count[ord(s2[i]) - ord('a')] -= 1
            
            # increase introduced char count
            s2Count[ord(s2[i+len(s1)]) - ord('a')] += 1

        return s1Count == s2Count   