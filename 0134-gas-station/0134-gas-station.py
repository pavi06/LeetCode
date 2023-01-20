class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        for i in range(len(gas)):    #calculating whether total gas is less than total cost
            total+=gas[i]-cost[i]
        if total<0:                   #if total cost is less then return -1
            return -1
        rem=ind=0
        for i in range(len(gas)):     #start from 0 index and check it is feasible to travel
            currgas=gas[i]+rem        #each time the gas and rem is added
            currcost=cost[i]          #cost is assigned to currcost var
            rem=currgas-currcost        #cal remainder
            if rem<0:                   #if rem less than 0 then move to next indx
                rem=0
                ind=i+1
        return ind                   #return the index 
                    
#O(n) complexity           
        