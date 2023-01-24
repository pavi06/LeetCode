class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total=0
        boxTypes.sort(key=lambda x:-x[1])
        for i in range(len(boxTypes)):
            if truckSize>0:
                if boxTypes[i][0] < truckSize:
                    total+=boxTypes[i][0]*boxTypes[i][1]
                    print(total)
                    truckSize-=boxTypes[i][0]
                else:
                    total+=truckSize*boxTypes[i][1]
                    break
        return total
        