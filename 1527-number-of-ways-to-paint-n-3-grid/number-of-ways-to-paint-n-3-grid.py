class Solution:
    def numOfWays(self, n: int) -> int:
        mod=10**9+7
        prev_2Different=6
        prev_3Different=6
        cur_2Different=0
        cur_3Different=0
        for i in range(n-1):
            cur_2Different=(3*prev_2Different+2*prev_3Different)%mod
            cur_3Different=(2*prev_2Different+2*prev_3Different)%mod
            prev_2Different=cur_2Different   
            prev_3Different=cur_3Different
        return (prev_2Different+prev_3Different)%mod    