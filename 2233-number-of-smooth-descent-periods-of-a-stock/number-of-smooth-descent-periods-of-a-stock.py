class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l=0
        if len(prices)==1:
            return 1
        ans=0    
        for i in range(1,len(prices)):
            if prices[i]!=prices[i-1]-1:
                ans+=(i-l)*(i-l+1)//2
                l=i
        ans+=(i-l+1)*(i-l+2)//2  
        return ans