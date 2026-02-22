class Solution:
    def binaryGap(self, n: int) -> int:
        c=cc=0
        while n:       
            if n%2:
                c=max(c,cc)
                cc=1
            else:
                if cc:
                    cc+=1
            n=n//2
        return c           