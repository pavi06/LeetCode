class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[float("inf") for i in range(len(word2)+1)] for i in range(len(word1)+1)]
        #backward dp
        for i in range(len(word1)+1):  #assigning value at the last column
            dp[i][len(word2)]=len(word1)-i
        for j in range(len(word2)+1):  #assignung value at the last row
            dp[len(word1)][j]=len(word2)-j
        #lets traverse
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1] #collect the diag cell val
                else:
                    dp[i][j] = 1 + min(dp[i][j+1],dp[i+1][j+1],dp[i+1][j]) #check all the right,bottom and diag cell
                    
        return dp[0][0]
                    