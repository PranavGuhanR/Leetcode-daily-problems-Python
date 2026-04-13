class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        i=start
        r=0
        while i+r<len(nums) and i-r>=0:
            if nums[i+r]==target or nums[i-r]==target:
                return r
            r+=1  

        if i-r<0:
            while True:
                if nums[i+r]==target:
                    return r
                r+=1    
        while True:
            if nums[i-r]==target:
                return r 
            r+=1                           