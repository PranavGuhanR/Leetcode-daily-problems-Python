class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        mj=[-1]*len(nums)
        mj[-1]=0
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if (abs(nums[i]-nums[j])<=target) and mj[j]!=-1:
                    mj[i]=max(mj[i],mj[j]+1)

        return mj[0]             
        