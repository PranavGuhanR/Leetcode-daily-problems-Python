class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        d=dict()
        for i in edges:
            if i[0] not in d:
                d[i[0]]=[i[1]]     
            else:
                d[i[0]].append(i[1])
            if i[1] not in d:
                d[i[1]]=[i[0]]     
            else:
                d[i[1]].append(i[0])   
        vis=[0]*(len(edges)+1)                     
        q=deque([1])  
        depth=-1 
        while q: 
            n=len(q)
            for i in range(n):
                c=q.popleft()
                vis[c-1]=1
                if c in d:
                    for i in d[c]:
                        if vis[i-1]!=1:
                            q.append(i)
            depth+=1
        if depth==1:
            return 1                
        return pow(2,depth-1,10**9+7)           