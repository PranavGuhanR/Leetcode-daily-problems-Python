class Solution:
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    def findSafeWalk(self, A: List[List[int]], health: int) -> bool:

        pq = [(A[0][0], 0, 0)]
        n=len(A)
        m=len(A[0])

        while pq:
            sf, i, j = heapq.heappop(pq)
            

            if i == n - 1 and j == m - 1:
                if sf<health:
                    return True
                return False     

            for dx, dy in self.dirs:
                x, y = i + dx, j + dy
                if ((min(x, y) >= 0) and (x < n) and (y < m) and (A[x][y]!=2)) :
                    heapq.heappush(pq, (sf+A[x][y], x, y))
                    A[x][y] = 2     