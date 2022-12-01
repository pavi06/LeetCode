class Solution:
    def interpret(self, command: str) -> str:
        s=command
        return s.replace("()","o").replace("(al)","al")
                
        