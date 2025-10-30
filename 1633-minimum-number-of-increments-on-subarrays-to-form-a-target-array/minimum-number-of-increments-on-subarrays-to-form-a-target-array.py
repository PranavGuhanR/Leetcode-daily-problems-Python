class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        p=0
        c=0
        for i in target:
            if i>p:
                c+=i-p
            p=i
        return c 