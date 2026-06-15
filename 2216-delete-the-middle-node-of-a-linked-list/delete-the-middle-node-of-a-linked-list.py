# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        fast=head
        slow=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev==None:
            return None            
        if slow!=None:
            prev.next=slow.next
        else:       
            prev.next=None
        return head    