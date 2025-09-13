class Solution:
    def maxFreqSum(self, s: str) -> int:
        dv=dict()
        for i in 'aeiou':
            dv[i]=0
        dc=dict()
        mc=mv=0
        for i in s:
            if (i not in dv) and (i not in dc):  
                dc[i]=1
                mc=max(mc,dc[i])
            elif i in dc:
                dc[i]+=1
                mc=max(mc,dc[i])
            else:
                dv[i]+=1
                mv=max(mv,dv[i])
        return mc+mv    