# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        ans=l[0]+l[-1]    
        for i in range(1,len(l)//2):
            ans=max(ans,l[i]+l[len(l)-1-i])
        return ans    