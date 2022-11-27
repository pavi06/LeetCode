class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist=10**10
        ind=-1
        for i,(x1,y1) in enumerate(points):
            if (x1==x or y1==y):
                s=abs(x-x1)+abs(y-y1)
                if s<min_dist:
                    ind=i
                    min_dist=s
        return ind
    
    