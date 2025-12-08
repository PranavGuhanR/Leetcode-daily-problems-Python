class Solution:
    d={}
    for i in range(1,251):    
        d[i**2]=i
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n):
            for j in range(i+1,n+1):
                print(i,j)
                if i**2+j**2 in self.d:
                    if self.d[i**2+j**2] <= n:
                        count+=1
        return 2*count                