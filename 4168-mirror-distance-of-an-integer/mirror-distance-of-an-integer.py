class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            s=str(n)
            rs="".join([s[i] for i in range(-1,-len(s)-1,-1)])
            return int(rs)
        return abs(n-reverse(n))    