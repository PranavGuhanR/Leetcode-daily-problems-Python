class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod=10**9+7
        fac={0:1}
        def f(n):
            if n in fac:
                return fac[n]
            fac[n]=(f(n-1)*(n%mod))%mod    
            return fac[n]
        for i in complexity[1::]:
            if i<=complexity[0]:
                return 0
        return f(len(complexity)-1)            