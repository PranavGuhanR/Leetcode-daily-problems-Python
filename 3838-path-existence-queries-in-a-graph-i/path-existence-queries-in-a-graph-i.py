class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group_count=0
        group_list=[0]*n
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>maxDiff:
                group_count+=1
            group_list[i]=group_count
        ans=[False]*len(queries)
        for i,query in enumerate(queries):  
            if group_list[query[0]]==group_list[query[1]]:
                ans[i]=True
            else:
                ans[i]=False
        return ans            