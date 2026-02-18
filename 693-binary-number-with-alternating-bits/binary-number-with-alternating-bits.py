class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cb=n%2
        n=n>>1
        while n:
            if cb==n%2:
                return False
            cb=n%2
            n=n>>1
        return True        
