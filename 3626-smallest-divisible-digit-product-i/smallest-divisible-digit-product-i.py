class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def p(N):
            cn=N
            pd=1
            while cn:
                pd*=cn%10
                cn//=10
            return pd     
        while p(n)%t:
            n+=1 
        return n          