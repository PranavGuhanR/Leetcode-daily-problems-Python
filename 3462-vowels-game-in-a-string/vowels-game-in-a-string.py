class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c=0
        for i in s:       
            if i in 'aeiou':
                c+=1
        if c==0:
            return False
        return True             