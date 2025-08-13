class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<0:
            return False
        c=1    
        while n>=c:
            if n==c:
                return True  
            c*=3
        return False         