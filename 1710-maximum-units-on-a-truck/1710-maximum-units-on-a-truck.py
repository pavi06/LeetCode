class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total=0
        boxTypes.sort(key=lambda x:-x[1]) #sorting the ele based on units and specify with minus to indicate desc order
        for i in range(len(boxTypes)):
            if truckSize>0:
                if boxTypes[i][0] < truckSize:
                    total+=boxTypes[i][0]*boxTypes[i][1]
                    truckSize-=boxTypes[i][0]
                else:
                    total+=truckSize*boxTypes[i][1]    #if truckSize is lessthan  boxSize
                    break
        return total
        