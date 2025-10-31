class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sd=0
        ss=0  
        n=len(nums)-2      
        for i in nums:
            sd+=i
            ss+=i*i
        sd-=n*(n-1)//2
        ss-=n*(n-1)*(2*n-1)//6
        pd=sd**2-ss
        sbd=(sd**2-2*pd)**0.5
        return [int(sbd+sd)//2,int(sd-sbd)//2]