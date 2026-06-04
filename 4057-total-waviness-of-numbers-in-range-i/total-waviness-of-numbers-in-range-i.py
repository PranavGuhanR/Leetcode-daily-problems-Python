class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def wn(n):
            if n<100:
                return 0
            p=n%10
            n//=10
            c=n%10
            n//=10
            nex=n%10
            w=0
            while n:
                if (c>p and c>nex):
                    w+=1
                elif(c<p and c<nex):
                    w+=1     
                p=c
                c=nex
                n//=10
                nex=n%10
            return w
        ans=0    
        for i in range(num1,num2+1):
            ans+=wn(i)  
        return ans    