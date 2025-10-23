class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s=list(int(i) for i in s)
        na=[0]*(len(s)-1)
        while len(na)>2:
            print(s,na)
            for i in range(len(na)):
                na[i]=(s[i]+s[i+1])%10
            s=na.copy()
            na.pop()  
        if (s[0]+s[1])%10==(s[1]+s[2])%10:
            return True
        return False        