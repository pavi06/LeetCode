class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:        #if totalgas is less then totalcost return -1
            return -1
        rem=ind=0
        for i in range(len(gas)):       #start from 0 index and check it is feasible to travel
            rem=(gas[i]+rem)-cost[i]    #cal remainder by adding gas and rem and sub cost
            if rem<0:                   #if rem less than 0 then move to next index
                rem=0
                ind=i+1
        return ind                   #return the index 
                    
#O(n) complexity  
#bruteforce O(n^2)=> 2for loop 
        