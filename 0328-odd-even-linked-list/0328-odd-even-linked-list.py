# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        odd=head
        oh=head
        even=head.next
        eh=head.next
        while(odd.next!=None and even.next!=None):
            odd.next=odd.next.next
            odd=odd.next
            if(even):
                even.next=even.next.next
                even=even.next
        odd.next=eh
        return oh
        