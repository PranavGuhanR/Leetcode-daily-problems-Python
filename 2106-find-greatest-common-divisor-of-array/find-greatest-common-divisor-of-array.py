class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(a,b):
            if a>b:
                a,b=b,a
            while a!=0:
                b%=a
                a,b=b,a
            return b      
        return GCD(min(nums),max(nums))         