class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        w = d + 1  
        lo, hi = {}, {} 
        for b in arr2:
            k = b // w
            lo[k], hi[k] = min(lo.get(k, b), b), max(hi.get(k, b), b)

        def far(a): 
            k = a // w
            return k not in lo and hi.get(k - 1, -inf) < a - d and lo.get(k + 1, inf) > a + d

        return sum(map(far, arr1))