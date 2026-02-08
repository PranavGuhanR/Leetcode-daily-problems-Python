# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(n):
            if n==None:
                return [0,1]
            r=[0,1]
            l=[0,1]
            if n.right:
                r=h(n.right)
            if n.left:  
                l=h(n.left)
            ba=1    
            if abs(l[0]-r[0])>1:
                ba=0
            return [max(l[0],r[0])+1,min(l[1]*r[1],ba)]
        l=[False,True]     
        return l[h(root)[1]]             