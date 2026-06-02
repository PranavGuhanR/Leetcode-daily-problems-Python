class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m=10000
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                if landStartTime[i]<waterStartTime[j]:
                    if landStartTime[i]+landDuration[i]>=waterStartTime[j]:
                        lm=landStartTime[i]+landDuration[i]+waterDuration[j]
                    else:
                        lm=waterStartTime[j]+waterDuration[j]
                else:
                    if waterStartTime[j]+waterDuration[j]>=landStartTime[i]:
                        lm=waterStartTime[j]+landDuration[i]+waterDuration[j]
                    else:
                        lm=landStartTime[i]+landDuration[i]                    
                m=min(m,lm)
        return m             