class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d=dict()
        for i in arr:
            n=i
            c=0
            while n:
                if n%2:
                    c+=1
                n//=2
            if c in d:
                d[c].append(i) 
            else:
                d[c]=[i]
        b=sorted(list(d.keys()))
        ans=[]
        for i in b:
            l=sorted(d[i])
            ans.extend(l)
        return ans    