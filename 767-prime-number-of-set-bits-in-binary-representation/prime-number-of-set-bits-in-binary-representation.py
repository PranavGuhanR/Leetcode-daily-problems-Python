class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        p={2,3,5,7,11,13,17,19,23}
        def ispnb(n):
            c=0
            while n:
                if n%2:
                    c+=1  
                n=n//2
            if c in p:
                return True
            return False
        ans=0    
        for i in range(left,right+1):
            if ispnb(i):
                ans+=1
        return ans    