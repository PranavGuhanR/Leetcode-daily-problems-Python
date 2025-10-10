class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        l=[0]*k
        for i in range(len(energy)):
            if  l[i%k]<0:
                l[i%k]=0
            l[i%k]+=energy[i]
        return max(l)        