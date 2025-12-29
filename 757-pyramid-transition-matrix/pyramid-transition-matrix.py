from collections import deque
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        di=dict()
        for i in allowed:
            if i[:2] not in di:
                di[i[:2]]=[i[2]]
            else:
                di[i[:2]].append(i[2])    
        def G(D,CS):
            if len(D)==len(CS)+1:
                if len(CS)==1:
                    return 1
                return G(CS,'')
            ad=D[len(CS):len(CS)+2]  
            if ad in di:  
                for i in di[ad]:
                    if G(D,CS+i):
                        return 1
                return 0
            return 0    
        if G(bottom,''):
            return True
        return False                              