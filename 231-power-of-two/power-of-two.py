class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pn=1
        for i in range(31):
            if pn==n:
                return True
            pn*=2
        return False                