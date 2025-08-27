class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])  # Get the dimensions of the grid
        
        @cache  # Memoization to optimize recursive calls
        def dfs(row, col, turn, direction, target):
            # Base case: Check boundaries and if the cell matches the target value
            if row not in range(n) or col not in range(m) or grid[row][col] != target:
                return 0
            
            # Toggle the target between 2 and 0 after each step
            target = 0 if grid[row][col] == 2 else 2
            
            # Move diagonally based on the direction
            if direction == 0:  # Top-left diagonal
                if turn:
                    return 1 + max(dfs(row - 1, col - 1, turn, 0, target), 
                                   dfs(row - 1, col + 1, False, 1, target))
                return 1 + dfs(row - 1, col - 1, turn, 0, target)
            
            elif direction == 1:  # Top-right diagonal
                if turn:
                    return 1 + max(dfs(row - 1, col + 1, turn, 1, target), 
                                   dfs(row + 1, col + 1, False, 2, target))
                return 1 + dfs(row - 1, col + 1, turn, 1, target)
            
            elif direction == 2:  # Bottom-right diagonal
                if turn:
                    return 1 + max(dfs(row + 1, col + 1, turn, 2, target), 
                                   dfs(row + 1, col - 1, False, 3, target))
                return 1 + dfs(row + 1, col + 1, turn, 2, target)
            
            else:  # Bottom-left diagonal
                if turn:
                    return 1 + max(dfs(row + 1, col - 1, turn, 3, target), 
                                   dfs(row - 1, col - 1, False, 0, target))
                return 1 + dfs(row + 1, col - 1, turn, 3, target)

        longest_v = 0  # Variable to store the longest V-diagonal length
        
        # Iterate through the grid to find starting points (cells with value 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Start DFS in all four diagonal directions
                    longest_v = max(longest_v, 
                        1 + max(dfs(i - 1, j - 1, True, 0, 2),  # Top-left
                                dfs(i - 1, j + 1, True, 1, 2),  # Top-right
                                dfs(i + 1, j + 1, True, 2, 2),  # Bottom-right
                                dfs(i + 1, j - 1, True, 3, 2))) # Bottom-left
        
        return longest_v