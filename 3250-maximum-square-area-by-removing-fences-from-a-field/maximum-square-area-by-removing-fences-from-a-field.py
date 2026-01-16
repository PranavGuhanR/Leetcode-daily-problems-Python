class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        s=set()
        hFences.extend([1,m])
        for i in hFences:
            for j in hFences[1::]:
                s.add(abs(i-j))
        vFences.extend([1,n])        
        m=0
        for i in vFences:
            for j in vFences[1::]:
                d=abs(i-j)
                if d in s:
                    if d>m:
                        m=d
        mod=10**9+7                
        if m==0:
            return -1
        return ((m%mod)**2)%mod                            