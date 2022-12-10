class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        uChar = {}
        
        for i in range(len(s)):
            if s[i] in uChar and start <= uChar[s[i]]:
                start = uChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            uChar[s[i]] = i

        return maxLength
        
            
        