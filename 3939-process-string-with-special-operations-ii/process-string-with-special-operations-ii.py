class Solution:
    def processStr(self, s: str, k: int) -> str:
        c=0
        for i in range(len(s)):
            if s[i]=="%":
                pass
            elif s[i]=="#":
                c*=2
            elif s[i]=="*":
                if c>0:
                    c-=1
            else:
                c+=1
        if c<k+1:
            return "."       
        f=k
        for i in range(len(s)-1,-1,-1):
            if s[i]=="%":
                f=c-1-f
            elif s[i]=="#":
                if f+1>c//2:
                    f-=c//2
                c//=2
            elif s[i]=="*":
                c+=1
            else:
                if c==f+1:
                    return s[i]
                c-=1
        return s[0]    