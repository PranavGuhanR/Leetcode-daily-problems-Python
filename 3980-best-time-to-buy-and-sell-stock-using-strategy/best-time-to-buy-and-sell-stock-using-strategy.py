class Solution:
    def maxProfit(self, p: List[int], s: List[int], k: int) -> int:
        L = len(p)
        Ans = 0
        for i in range(L):
            Ans += p[i] * s[i]
        C=Ans
        for r in range(L):
          if r>k-1:
            C+=p[r-k]*s[r-k]
            C-=p[r-k//2]
          if r<k//2:
            C+=(p[r]*(-1*s[r]))
          else:
            C+=(p[r]*(-1*s[r]))
            C+=p[r]
          if r>=k-1:
            Ans=max(C,Ans)
        return Ans