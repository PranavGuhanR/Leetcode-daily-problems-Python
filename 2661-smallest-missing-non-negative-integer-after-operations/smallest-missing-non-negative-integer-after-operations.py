class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        lv=[0]*value
        for i in range(len(nums)):
            lv[nums[i]%value]+=1
        l=[]
        for i in range(value):
            l.append([lv[i],i]) 
        l.sort()
        return l[0][0]*value+l[0][1]     