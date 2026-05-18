class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dq=deque([0])
        l=1
        j=0
        indq=[0]*len(arr)
        indq[0]=1
        d=dict()

        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]].add(i)
            else:
                d[arr[i]]=set([i]) 

        def adsv(V,I):
            c=0
            l=list(d[V])
            for e in l:
                if e!=I:
                    if indq[e]!=1:
                        indq[e]=1
                        dq.append(e)
                        c+=1
                    else:
                        d[V].remove(e)    
            return c

        while dq:
            nl=0
            for i in range(l):
                c=dq.popleft()
                if c==len(arr)-1:
                    return j
                if c-1>=0 and indq[c-1]!=1:
                    nl+=1
                    indq[c-1]=1
                    dq.append(c-1)     
                if c+1<len(arr) and indq[c+1]!=1:
                    nl+=1
                    indq[c+1]=1
                    dq.append(c+1) 
                nl+=adsv(arr[c],c)
            l=nl 
            j+=1   