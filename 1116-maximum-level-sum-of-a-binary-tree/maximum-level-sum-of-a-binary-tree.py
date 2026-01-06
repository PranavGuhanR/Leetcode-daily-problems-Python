# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m=root.val
        lvl=1
        c=1
        q=deque([root])
        c_lvl=1
        while q:
            s=0
            for i in range(c):
                e=q.popleft()
                s+=e.val
                if e.left:
                    q.append(e.left)  
                if e.right:
                    q.append(e.right)   
            if s>m:
                m=s
                lvl=c_lvl
            c=len(q)
            c_lvl+=1
        return lvl               