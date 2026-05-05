# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def l(h):
            c=0
            h=head
            while h:
                c+=1
                h=h.next
            return c  

        if head==None:
            return None
            
        n=l(head)     
        k=k%n

        if k==0:
            return head

        sn=head
        cn=head
        
        for i in range(n-k):
            pn=cn
            cn=cn.next

        pn.next=None

        ans=cn
        while cn.next:
            cn=cn.next

        cn.next=sn

        return ans        