class Solution:
    def maxProduct(self, n: int) -> int:
        sm=-1
        m=-1
        while n:
            if n%10>=m:
                sm=m
                m=n%10
            elif n%10>sm:
                sm=n%10
            n//=10    
        return m*sm            

