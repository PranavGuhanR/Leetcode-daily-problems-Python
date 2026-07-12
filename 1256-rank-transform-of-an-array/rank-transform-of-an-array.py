class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        na=sorted(arr)
        d=dict()
        r=1
        for i in na:
            if i not in d:
                d[i]=r
                r+=1
        ans=[0]*(len(arr))
        for i in range(len(arr)):
            ans[i]=d[arr[i]]
        return ans                