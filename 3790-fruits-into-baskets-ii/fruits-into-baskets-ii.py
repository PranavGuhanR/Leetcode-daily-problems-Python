class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        p=[0]*len(baskets)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if (not p[j]) and (baskets[j]>=fruits[i]):
                    p[j]=1
                    c+=1
                    break
        return len(baskets)-c            