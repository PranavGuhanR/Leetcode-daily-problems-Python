class Solution:
    def compress(self, chars: List[str]) -> int:
        pc=chars[0]
        i=1
        cp=1
        c=1
        while i<len(chars):
            if chars[i]!=pc:
                if c>1:
                    d=str(c)
                    dl=len(d)
                    for j in range(i-1,i-c+dl,-1):
                        del chars[j]
                    for j in range(cp,cp+dl):
                        chars[j]=d[j-cp]    
                    i=cp+dl
                cp=i+1
                pc=chars[i]
                c=1
                i+=1
            else:
                c+=1
                i+=1    
        if c>1:
            d=str(c)
            dl=len(d)
            for j in range(i-1,i-c+dl,-1):
                del chars[j]
            for j in range(cp,cp+dl):
                chars[j]=d[j-cp]    
            i=cp+dl 
        return len(chars)                 