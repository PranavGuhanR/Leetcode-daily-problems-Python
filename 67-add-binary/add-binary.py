class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<=len(b):
            a,b=b,a
        b=b.zfill(len(a))
        c=0
        s=[]
        for i in range(-1,-len(a)-1,-1):
            d=(int(a[i])+int(b[i]))+c
            s.append(bin(d)[-1])
            if d>1:
                c=1
            else:
                c=0    
        if c:
            s.append(str(c)[-1])   
        return ''.join(s[::-1])   