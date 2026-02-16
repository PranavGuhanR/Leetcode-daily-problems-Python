class Solution:
    def reverseBits(self, n: int) -> int:
        p=31
        ans=0
        for i in range(32):
            if n%2:
                ans+=2**p
            n=n>>1
            p-=1
        return ans        
