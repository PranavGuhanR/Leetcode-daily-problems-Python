class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: (-int(x[1]), x[0]), reverse=True)
        ans = [0]*numberOfUsers
        online = [0]*numberOfUsers
        for evt, time, ids in events: 
            time = int(time)
            if evt == "MESSAGE": 
                if ids == "ALL": 
                    for i in range(numberOfUsers): ans[i] += 1
                elif ids == "HERE": 
                    for i in range(numberOfUsers): 
                        if online[i] <= time: ans[i] += 1
                else: 
                    for id in ids.split(): 
                        ans[int(id.strip("id"))] += 1                    
            else: online[int(ids)] = time + 60
        return ans 