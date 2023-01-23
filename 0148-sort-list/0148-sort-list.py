# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:   #if the list has one or no ele then return it 
            return head
        l=head
        r=self.getMid(head)  #finding the mid and breaking the link
        temp=r.next
        r.next=None
        r=temp
        
        left=self.sortList(l)      #dividing recursively
        right=self.sortList(r)
        return self.merge(left,right)
        
    def getMid(self,head):      #To find the mid of the list to divide it
        slow,fast=head,head.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
        
    def merge(self,l,r):         #merge function 
        tail=dummy=ListNode()
        while(l and r):
            if l.val>r.val:
                tail.next=r
                r=r.next
            else:
                tail.next=l
                l=l.next
            tail=tail.next
        if l:
            tail.next=l
        if r:
            tail.next=r
        return dummy.next
#perform merge sort but dividing and merging it       