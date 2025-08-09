class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ma=0
        while l<r:
            if height[l]<height[r]:
                ma=max(ma,height[l]*(r-l))
                l+=1
            else:
                ma=max(ma,height[r]*(r-l))
                r-=1
        return ma    