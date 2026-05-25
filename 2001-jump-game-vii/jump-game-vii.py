class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        d=deque([0])
        mr=0        
        while d:
            c=d.popleft()
            for i in range(max(mr+1,c+minJump),min(c+maxJump+1,len(s))):
                if s[i]=='0':
                    if i==len(s)-1:
                        return True
                    d.append(i)
            mr=c+maxJump        
        return False            