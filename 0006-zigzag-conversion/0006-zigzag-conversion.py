class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #basecase
        if  numRows==1:
            return s
        res=""
        for r in range(numRows):
            jump=(numRows-1)*2
            for i in range(r,len(s),jump):#start from the index 0, 1, 2,..
                res+=s[i]
                if(r>0 and r<numRows-1 and i+jump-2*r<len(s)): #executed for middle row
                    res+=s[i+jump-2*r]
        return res
                    
                
#1st row-> 6 jumps((no,of.rows-1)*2)
#2nd row-> 4,6 i.e dec 2 on each row
#3rd row-> 2,6 
        