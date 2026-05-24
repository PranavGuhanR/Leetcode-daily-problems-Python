class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        l=[]
        ans=1
        for i in range(len(arr)):
            heapq.heappush(l,(arr[i],i))
        D={}
        for i in range(len(arr)):
            p=heapq.heappop(l)
            v=p[0]
            idx=p[1]
            mi=max(0,idx-d)
            ma=min(idx+d,len(arr)-1)
            mcj=1
            for j in range(idx-1,mi-1,-1):
                if arr[j]<arr[idx]:
                    mcj=max(D[j]+1,mcj)
                else:
                    break    
            for j in range(idx+1,ma+1):
                if arr[j]<arr[idx]:
                    mcj=max(D[j]+1,mcj) 
                else:
                    break    
            D[idx]=mcj       
            ans=max(ans,mcj)   
        return ans                        