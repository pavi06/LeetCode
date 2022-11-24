class Solution:
    def average(self, salary: List[int]) -> float:
        mi=min(salary)
        ma=max(salary)
        s=sum(salary)-mi-ma
        return s/(len(salary)-2)
        