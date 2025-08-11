class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers=[0]
        a=0
        while n:
            if n%2:
                powers.append(powers[-1]+a)
            a+=1   
            n=n>>1   
        ans=[0]*len(queries)     
        for i in range(len(queries)):
            ans[i]=pow(2,powers[queries[i][1]+1]-powers[queries[i][0]],10**9+7)
        return ans    