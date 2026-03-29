class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if set([s1[0],s1[2]])==set([s2[0],s2[2]]):
            if set([s1[1],s1[3]])==set([s2[1],s2[3]]):
                return True
        return False        