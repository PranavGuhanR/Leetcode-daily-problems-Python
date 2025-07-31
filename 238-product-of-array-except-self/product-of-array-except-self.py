class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=[1]*len(nums)
        l=[0]*len(nums)
        p=1
        for i in range(len(nums)-1,0,-1):
            s[i-1]=s[i]*nums[i] 
        for i in range(len(nums)):
            l[i]=p*s[i]  
            p*=nums[i]   
        return l           