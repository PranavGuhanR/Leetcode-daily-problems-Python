class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def GCD(a,b):
            if b>a:
                a,b=b,a
            while a!=0:
                b%=a
                a,b=b,a
            return b
 
        m=nums[0]
        prefixGcd=[0]*len(nums)
        for i in range(len(nums)):
            m=max(m,nums[i])
            prefixGcd[i]=GCD(m,nums[i])
        prefixGcd.sort()
        l=0
        r=len(nums)-1
        s=0
        while l<r:
            s+=GCD(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1

        return s                    