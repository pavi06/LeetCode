class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        phash = Counter(p)                  #counter for p string
        shash = Counter(s[:len(p)-1])       #counter till first len(p)-1 character of s string
        for i in range(len(p)-1,len(s)):    #from index 2 to till end
            shash[s[i]] += 1                #add char one by one 
            if shash == phash:    
                res.append(i-len(p)+1)      #checks whether both are equal
            shash[s[i-len(p)+1]] -= 1       #reduce the count of  the start index character
            if shash[s[i-len(p)+1]] == 0:
                del shash[s[i-len(p)+1]]    #if reduced count becomes zero then it deletes from the counter
        return res

            
            
        