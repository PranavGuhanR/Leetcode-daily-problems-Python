class Solution:
    def minimumPushes(self, s: str) -> int:
        d=dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        if len(d)<9:
            return len(s)
        l=list(d.values()) 
        l.sort(reverse=True)
        if len(d)<17:
            return len(s)+sum(l[8:len(d)]) 
        elif len(d)<25:    
            return len(s)+sum(l[8:16])+2*sum(l[16:len(d)])   
        return len(s)+sum(l[8:16])+2*sum(l[16:24])+3*sum(l[24:len(d)])     