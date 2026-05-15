class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        pl=-1
        if nums[l]<nums[r]:
            return nums[l]
        while l>=0 and l!=r-1:
            print(l,r)
            if nums[l]>nums[r]:
                m=(l+r)//2
                if nums[m]>nums[r]:
                    pl=l
                    l=m
                else:
                    r=m
            else:
                r=l
                l=pl 
                pl=l   

        return nums[r]