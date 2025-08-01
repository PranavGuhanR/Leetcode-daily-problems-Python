class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        elif n==2:
            return [[1],[1,1]]    
        else:
            prs=self.generate(n-1)
            prs+=[[1]*n]
            for i in range(1,n-1):
                prs[n-1][i]=prs[n-2][i-1]+prs[n-2][i]
            return prs   