class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans=0
        if len(nums)==1:
            return ans
        while True:
            iss=1
            ms=nums[0]+nums[1]
            ss=0
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    iss=0
                s=nums[i]+nums[i-1]    
                if s<ms:
                    ms=s
                    ss=i-1
            if iss:
                return ans
            ans+=1
            if len(nums)==2:
                return ans
            if len(nums)>ss+2:    
                nums=nums[:ss]+[ms]+nums[ss+2::]
            else:
                nums=nums[:ss]+[ms]                     