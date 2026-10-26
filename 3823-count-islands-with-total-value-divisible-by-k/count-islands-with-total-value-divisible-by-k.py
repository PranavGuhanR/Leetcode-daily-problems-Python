class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            row = grid[i]
            for j in range(n):
                if row[j]:
                    total = row[j]
                    row[j] = 0
                    stack = [(i, j)]
                    
                    while stack:
                        r, c = stack.pop()
                        if r > 0 and grid[r - 1][c]:
                            total += grid[r - 1][c]
                            grid[r - 1][c] = 0
                            stack.append((r - 1, c))
                        if r + 1 < m and grid[r + 1][c]:
                            total += grid[r + 1][c]
                            grid[r + 1][c] = 0
                            stack.append((r + 1, c))
                        if c > 0 and grid[r][c - 1]:
                            total += grid[r][c - 1]
                            grid[r][c - 1] = 0
                            stack.append((r, c - 1))
                        if c + 1 < n and grid[r][c + 1]:
                            total += grid[r][c + 1]
                            grid[r][c + 1] = 0
                            stack.append((r, c + 1))
                            
                    if total % k == 0:
                        count += 1
                        
        return count