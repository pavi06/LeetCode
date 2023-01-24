class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        print(dp)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                print(dp[j],end=": ")
                print(s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    print(dp)
                    break
                    
        return dp[-1]
            
                
                