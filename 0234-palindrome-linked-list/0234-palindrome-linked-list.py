# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        if l==l[::-1]:
            return True
        else:
            return False
        
        