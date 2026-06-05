class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def count(x: int) -> int:
            if x == 0:
                return 0
                
            # Convert number to a list of digits
            d = [int(digit) for digit in str(x)]
            
            # @cache automatically handles the memoization (replaces the 6D dp array)
            @cache
            def solve(pos: int, sum_val: int, prv2: int, prv: int, small: bool, nz: bool) -> int:
                # Base case: reached the end of the digits
                if pos == len(d):
                    return sum_val
                    
                lim = 9 if small else d[pos]
                ans = 0
                
                for i in range(lim + 1):
                    nsmall = small or (i < d[pos])
                    nnz = nz or (i != 0)
                    
                    if nnz:
                        nprv2 = prv
                        nprv = i
                        nsum = sum_val
                        
                        # 10 acts as the uninitialized dummy state for previous digits
                        if prv2 != 10 and prv != 10:
                            # int(True) evaluates to 1, int(False) evaluates to 0
                            nsum += int(prv2 < prv and prv > i)
                            nsum += int(prv2 > prv and prv < i)
                            
                        ans += solve(pos + 1, nsum, nprv2, nprv, nsmall, nnz)
                    else:
                        ans += solve(pos + 1, sum_val, prv2, prv, nsmall, nnz)
                        
                return ans
                
            # Initial call: pos=0, sum=0, prv2=10, prv=10, small=False, nz=False
            return solve(0, 0, 10, 10, False, False)

        return count(num2) - count(num1 - 1)