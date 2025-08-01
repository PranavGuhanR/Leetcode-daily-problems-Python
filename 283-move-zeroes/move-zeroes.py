class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        e=len(nums)-2
        s=len(nums)-2
        while s>=0:
            if nums[s]==0:
                for i in range(s,e+1):
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                e-=1    
            s-=1     
        return nums       