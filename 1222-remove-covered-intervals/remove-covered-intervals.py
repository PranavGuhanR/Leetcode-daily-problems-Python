class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        s=set()
        for i in range(len(intervals)):
            f1=1
            f2=1
            re=set()
            for e in s:
                if e[0]>=intervals[i][0] and e[1]<=intervals[i][1]:
                    re.add(tuple(e))
                    f1=0
                if f1:
                    if e[0]<=intervals[i][0] and e[1]>=intervals[i][1]:  
                        f2=0
                        break
            if f2:
                s.add(tuple(intervals[i]))          
            s=s.difference(re)  
        return len(s)              