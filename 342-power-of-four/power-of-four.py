class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False    
        c=1       
        while c<=n:
            if c==n:
                return True
            c*=4
        return False                 