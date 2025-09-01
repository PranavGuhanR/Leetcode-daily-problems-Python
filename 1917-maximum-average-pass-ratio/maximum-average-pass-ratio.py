import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        d={}
        h=[]
        for i in range(len(classes)):
            pri=(classes[i][0]+1)/(classes[i][1]+1)-classes[i][0]/classes[i][1]
            heapq.heappush(h,-1*pri)
            if pri in d:
                d[pri].append(i)
            else:
                d[pri]=[i] 
        for i in range(extraStudents):
            hpri=heapq.heappop(h)
            idx=d[-1*hpri][-1]
            if len(d[-1*hpri])==1:
                del d[-1*hpri]
            else:    
                d[-1*hpri].pop()
            classes[idx][0]+=1
            classes[idx][1]+=1    
            npr=(classes[idx][0]+1)/(classes[idx][1]+1)-classes[idx][0]/classes[idx][1]
            heapq.heappush(h,-1*npr)
            if npr in d:
                d[npr].append(idx)
            else:
                d[npr]=[idx]    
        apr=0        
        for i in classes:
            apr+=i[0]/i[1]    
        apr/=len(classes)
        return round(apr,5)     