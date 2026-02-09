# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def T2L(n,l):
            if n.left:
                T2L(n.left,l)
            l.append(n.val)
            if n.right:
                T2L(n.right,l) 
        L=[]           
        T2L(root,L) 
        def L2T(rn,s,e):
            rn.val=L[(s+e)//2]
            if s<=(s+e)//2-1:
                rn.left=TreeNode()
                L2T(rn.left,s,(s+e)//2-1)
            if (s+e)//2+1<=e:
                rn.right=TreeNode()
                L2T(rn.right,(s+e)//2+1,e)  
        root1=TreeNode()         
        L2T(root1,0,len(L)-1)           
        return root1