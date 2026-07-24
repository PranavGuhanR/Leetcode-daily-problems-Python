class Solution:
    def uniqueXorTriplets(self, V: List[int]) -> int:
        X2 = {0}                                
        X3 = set(V)                            

        k = 1 << max(V).bit_length()

        while V:
            v = V.pop()                         

            X3 |= {v ^ x2 for x2 in X2}         
            X2 |= {v ^ vv for vv in V}          
            
            if len(X3) == k: break
        
        return len(X3)