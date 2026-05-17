class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        vis=[0]*len(arr)
        q=deque()
        q.append(start)
        if arr[start]==0:
            return True
        while q:
            c=q.popleft()
            vis[c]=1
            if c-arr[c]>=0 and vis[c-arr[c]]==0:
                if arr[c-arr[c]]==0:
                    return True
                q.append(c-arr[c])
            if c+arr[c]<=len(arr)-1 and vis[c+arr[c]]==0:
                if arr[c+arr[c]]==0:
                    return True                
                q.append(c+arr[c])                

        return False        