class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        dn=n
        while dn:
            s+=dn%10
            p*=dn%10
            dn//=10
        return n%(p+s)==0    