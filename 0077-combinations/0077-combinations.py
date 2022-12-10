# from itertools import combinations 

#backstrack --->  decision tree

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # l=[]
        # for i in range(1,n+1):
        #     l.append(i)
        # c=combinations(l,k)
        # return c
        
        res=[] #list to append the combinations
        def backtracknum(start,comb):
            if len(comb)==k:
                res.append(comb.copy()) #appending the combination if it attains its maxlen : 'K'
                return
            
            for i in range(start,n+1):
                comb.append(i)   #adding the element to the list
                backtracknum(i+1,comb)    #recursive call to check and add element
                comb.pop()       #after the comb is found, remove the last element to make another comb. 
          
        backtracknum(1,[])
        return res