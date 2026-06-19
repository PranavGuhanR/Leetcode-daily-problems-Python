class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=0
        ca=0
        for i in gain:
            ca+=i
            m=max(m,ca)    
        return m       