class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(k):
            for i in range(k//2):
                grid[x+i][y+j],grid[x+k-1-i][y+j]=grid[x+k-1-i][y+j],grid[x+i][y+j]

        return grid     