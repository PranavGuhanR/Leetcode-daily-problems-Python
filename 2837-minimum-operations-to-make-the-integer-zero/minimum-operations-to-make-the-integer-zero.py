class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1<num2:
            return -1
        for i in range(60):
            f=num1-(num2*(i+1))
            if f<1:
                return -1
            cmi=cma=0
            p2=1
            while f!=0:
                cmi+=f%2
                if f%2:
                    cma+=p2 
                f=f>>1
                p2*=2
            if cmi<=i+1<=cma:
                return i+1
        return -1            