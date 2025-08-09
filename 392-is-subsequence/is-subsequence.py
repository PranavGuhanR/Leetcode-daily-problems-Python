class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp=0
        for i in s:
            p=t[sp:].find(i)
            if p+1:
                sp+=p+1
            else:
                return False
        return True            
