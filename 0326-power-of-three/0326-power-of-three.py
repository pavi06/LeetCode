class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n==0 or n<0):
            return False
        while(n%3==0):   #remainder is checked 
            n/=3         #dividing by 3 --> will get the quotient
        if(n==1):      
            return True
            
        