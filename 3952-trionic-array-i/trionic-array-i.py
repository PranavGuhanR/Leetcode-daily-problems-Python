class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums)==3:
            return False
        n=nums[0]
        i=1
        c1=0
        while n<nums[i]:
            n=nums[i]
            i+=1
            c1+=1
            if i==len(nums)-1:
                return False
        if c1==0:
            return False 
        c2=0           
        while n>nums[i]:
            n=nums[i]
            i+=1 
            c2+=1
            if i==len(nums):
                return False
        if c2==0:
            return False        
        while n<nums[i]:
            n=nums[i]
            i+=1
            if i==len(nums):
                return True       
        return False                         