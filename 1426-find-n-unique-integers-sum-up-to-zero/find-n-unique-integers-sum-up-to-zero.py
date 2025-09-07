class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2:
            return [i for i in range(-1*(n//2),n//2+1)]
        l=[i for i in range(-1*(n//2),0)]
        for i in range(1,n//2+1):
            l.append(i)
        return l      