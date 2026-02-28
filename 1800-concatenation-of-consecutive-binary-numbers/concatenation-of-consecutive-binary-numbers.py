class Solution:
    def concatenatedBinary(self, n: int) -> int:
        fnnl=2
        pwf=2
        v=0
        mod=10**9+7
        for i in range(n):
            if i+1>=fnnl:
                pwf=(pwf*2)%mod
                fnnl*=2
            v=((v*pwf)%mod+i+1)%mod
        return v        