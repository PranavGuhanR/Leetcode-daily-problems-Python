class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l=1000
        r=-1000
        t=1000
        b=-1000
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    l=min(l,j)
                    r=max(r,j)
                    t=min(t,i)
                    b=max(b,i)
        if t-b==1000:
            return 0
        return (r-l+1)*(b-t+1)                