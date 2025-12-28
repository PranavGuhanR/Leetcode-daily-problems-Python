class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cs=0
        ans=0
        cne=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    ans+=(len(grid)-i)*(cne-j)
                    cne=j
                    if j==0:
                        return ans
                    else:
                        break
        return ans                    