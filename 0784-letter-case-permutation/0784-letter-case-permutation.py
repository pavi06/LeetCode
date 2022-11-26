class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for c in s:
            if c.isalpha():
                res = [i+j for i in res for j in [c.upper(), c.lower()]]
            else:
                res = [i+c for i in res]
        return res
        