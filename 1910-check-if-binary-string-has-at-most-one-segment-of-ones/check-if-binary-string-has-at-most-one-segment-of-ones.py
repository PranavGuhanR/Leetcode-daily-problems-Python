class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c=0
        for i in range(len(s)-1):
            if int(s[i])^int(s[i+1]):
                c+=1
                if c==2:
                    return False
        return True                 