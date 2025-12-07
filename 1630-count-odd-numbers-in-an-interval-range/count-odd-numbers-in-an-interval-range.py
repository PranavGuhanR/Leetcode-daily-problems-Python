class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=high-low+1
        ans=count//2
        if count%2:
            if low%2:
                ans+=1
        return ans        