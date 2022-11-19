# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head);
        fastpt=dummy
        slowpt=dummy
        for i in range(n):
            fastpt=fastpt.next
        while(fastpt.next):
            fastpt=fastpt.next
            slowpt=slowpt.next
        slowpt.next=slowpt.next.next
        return dummy.next
            
            
        