class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)
        
        ans = float('inf')
        
        for pos in positions.values():
            if len(pos) < 3:
                continue
            
            # For sorted indices a < b < c:
            # |a-b| + |b-c| + |c-a| = (b-a) + (c-b) + (c-a) = 2*(c-a)
            # So we just need the minimum span of any 3 consecutive positions.
            for i in range(len(pos) - 2):
                ans = min(ans, 2 * (pos[i + 2] - pos[i]))
        
        return ans if ans != float('inf') else -1