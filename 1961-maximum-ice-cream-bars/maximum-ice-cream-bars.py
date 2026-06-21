class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ar=[0]*(10**5)
        for e in costs:
            if e<=coins:
                ar[e-1]+=1
        ans=0        
        for i,v in enumerate(ar):
            if v>coins:
                return ans
            c=min(coins//(i+1),v)
            ans+=c
            coins-=c*(i+1)   
        return ans