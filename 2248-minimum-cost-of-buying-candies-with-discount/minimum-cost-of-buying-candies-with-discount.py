class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost,reverse=True)
        ans=0
        for i in range(len(cost)):
            if (i+1)%3==0:
                continue
            ans+=cost[i]
        return ans        