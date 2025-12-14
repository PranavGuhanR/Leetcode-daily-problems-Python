class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count_s=0
        n_ways=1
        cl=0
        cr=0
        mod=10**9+7
        for i in range(len(corridor)):
            if corridor[i]=='S':
                if (count_s!=0 and count_s%2==0):
                    n_ways=((n_ways%mod)*((i-l)%mod))%mod
                elif count_s%2:
                    l=i
                count_s+=1
        if count_s%2 or count_s==0:
            return 0
        if count_s==2:
            return 1
        return n_ways                                