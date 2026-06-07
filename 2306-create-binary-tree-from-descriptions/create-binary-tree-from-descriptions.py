# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d=dict()
        re=set()
        rn=set()
        for i in range(len(descriptions)):
            if descriptions[i][0] in d:
                pn=d[descriptions[i][0]] 
            else:
                pn=TreeNode(descriptions[i][0]) 
                d[descriptions[i][0]]=pn
                re.add(pn)
            if descriptions[i][1] in d:
                cn=d[descriptions[i][1]] 
                re.discard(cn)
            else:
                cn=TreeNode(descriptions[i][1]) 
                d[descriptions[i][1]]=cn
                re.discard(cn)
            if descriptions[i][2]==1:
                pn.left=cn
            else:
                pn.right=cn

        return list(re)[0]