# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s=dict()
        def su(n):
            if n in s:
                return s[n]
            sm=n.val
            if n.left:
                sm+=su(n.left)  
            if n.right:
                sm+=su(n.right)  
            s[n]=sm
            return sm
        q=deque([root])
        m=0
        while q:
            c=q.popleft()
            cp=su(c)*(su(root)-su(c))
            if cp>m:
                m=cp
            if c.left:    
                q.append(c.left)    
            if c.right:    
                q.append(c.right)  
        return m%(10**9+7)                   