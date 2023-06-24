class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr=(hour*30)+(minutes/60)*30
        mi=minutes*6
        angle=abs(hr-mi)
        return min(angle,360-angle)
        