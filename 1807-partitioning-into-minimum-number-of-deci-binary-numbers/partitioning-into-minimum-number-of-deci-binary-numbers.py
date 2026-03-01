class Solution:
    def minPartitions(self, n: str) -> int:
        m=1
        for i in n:
            if int(i)>m:
                m=int(i)
        return m        